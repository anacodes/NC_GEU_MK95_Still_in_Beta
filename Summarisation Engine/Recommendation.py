from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


## Function to provide recommendation to a person based on matching between person's skills and skills mentioned in job descriptions.

## Input -
    # Resume - List of string of skills extracted from resume of each person
    # JobDesc - List of string of skills extracted from each JD
    
    ### The skills of a Person should be in a string, instead of a list

## Output - List indicating the index of job which matched to each user
            # If choice[i] != -1 :- Person i matched with job 'choice[i]' the most
            # If choice[i] == -1 :- Person i did not match with any job

def Recommendation(Resume, JobDesc):

    ##--Combining both parts to run the cosine similarity---##
    Resume_and_JD = []
    for x in Resume:
        Resume_and_JD.append(x)

    for x in JobDesc:
        Resume_and_JD.append(x)

    startIndex = len(Resume) # This the index from where JD's begin in the combined list

    ##-----------Combining part ends--------------##


    ##-----Cosine similarity part starts---------##

    count_vectorizer = CountVectorizer(stop_words='english')
    count_vectorizer = CountVectorizer()

    sparse_matrix = count_vectorizer.fit_transform(Resume_and_JD)
    doc_term_matrix = sparse_matrix.todense()

    df = pd.DataFrame(doc_term_matrix, columns=count_vectorizer.get_feature_names())
    result = cosine_similarity(df, df)

    choice = []
    for i in range(len(Resume)):

        max_score = 0.1   #Threshold being set to 0.1
        curr_choice = -1
        for j in range(startIndex, len(result)):
            if result[i][j] > max_score:
                max_score = result[i][j]
                curr_choice = j - startIndex

        choice.append(curr_choice)     # if curr_choice == -1, no relevant jobs were found for the user
        
    return choice

    ##-----Cosine similarity part ends---------##

