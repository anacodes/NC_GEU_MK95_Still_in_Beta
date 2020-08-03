import sys
import os
from PyPDF2 import PdfFileReader
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from docx import *
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
import nltk
from io import StringIO
from summa import summarizer
from summa import keywords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pyresparser import ResumeParser
import pandas as pd
import numpy as np
import re
import warnings
warnings.filterwarnings("ignore")

from . import VacancyExtract, DateExtract, SalaryExtract, JobTitleExtract


def convert_pdf_to_txt(path, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    infile = open(path, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    sample = text
    return sample


def iter_block_items(parent):
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def extract_jd(file_type, file_path):
    # file_type = "pdf"  #'pdf' or 'docx'
    # file_path = 'C:\\Users\\Toshit\\Desktop\\JD\\g.pdf'
    print(os.path.abspath(os.curdir))
    # os.chdir("..")
    data = {}
    with open(file_path, 'rb') as file:
        text = ""
        if (file_type == "pdf"):
            pdf = PdfFileReader(file)
            number_of_pages = pdf.getNumPages()
            text = convert_pdf_to_txt(file_path,
                                      pages=range(0, number_of_pages))
        elif (file_type == "docx"):
            docx = Document(file_path)
            for block in iter_block_items(docx):
                if isinstance(block, Paragraph):
                    text += (block.text)
                elif isinstance(block, Table):
                    for row in block.rows:
                        for cell in row.cells:
                            for paragraph in cell.paragraphs:
                                text += (paragraph.text)
            # print(text)
            # text = " ".join(text.split())
            # text = re.sub(' +', ' ', text)
            # text = re.sub('\s{2,}', ' ', text)
            # print(list(text.split()))

        #text is a string
        summary_ratio = 0.3
        summary_words = 300
        summary_final = summarizer.summarize(
            text, ratio=summary_ratio)  #for words , words = summary_words
        summary_list = summary_final.split()
        summary_final_list = []
        for item in summary_list:
            if(item[0]=='\\' or (item=="\uf0b7") or (item=="\uf077")):
                continue
            else:
                summary_final_list.append(item)
        summary_final = " ".join(summary_final_list)
        data["job_summary"] = summary_final

        ### Extracting Skills Begins ###
        #remove stop_words from text :
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        filtered_text = [w for w in word_tokens if not w in stop_words]  #list
        filtered_text = " ".join(filtered_text)  #string
        # print("Summary :\n",summary_final)
        '''Extract Skills'''
        skill_dict = ResumeParser(file_path).get_extracted_data()
        data["skills"] = (skill_dict["skills"])
        data["total_vacancy"] = VacancyExtract.getVacancy(text)
        data["deadline"] = DateExtract.getDate(text)
        found_locations = []

        os.chdir('recruiter')
        database = pd.read_csv("pincode(reduced).csv",
                               sep=',',
                               engine='python')
        location_list = database['District'].unique()
        dictt = {}
        for item in location_list:
            item = str(item).lower()
            dictt[item] = True
        for item in filtered_text.split():
            if item.lower() in dictt.keys():
                found_locations.append(item)
        found_locations = " ".join(found_locations)
        data["location"] = found_locations
        data["salary"] = SalaryExtract.getSalary(text)
        data["job_title"] = JobTitleExtract.getJobTitle(text) 
        os.chdir('..')
        print(data)   
        return data