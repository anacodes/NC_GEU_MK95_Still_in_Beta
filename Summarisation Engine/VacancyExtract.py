def chkVac(s):

    # To handle cases like xxxx-zzzz 
    for x in s:           
        if x[-1] == '.' or x[-1] == ',':
            x = x[0:-1]

        if x.find('-') != -1 and x.find('-') != 0 and x.find('-') != len(x) - 1:
            ok = True
            for y in x:
                if y.isdigit() == False and y != '-':
                    ok = False

            if ok:
                return x


    ## Remaining cases to handle :-

    # To handle cases like xxxx - yyyy
    # To handle cases like xxx
    # To handle cases like vacancy-xxxx



    # Salary not found
    return ''                     


 
def getVacancy(s, d):
    s = s.lower()
    l = s.split()

    for i in range(len(l)):
        if l[i] in d or l[i][0:-1] in d:
            lo = max(0, i - 5)
            hi = min(len(l) - 1, i + 5)
            res = chkVac(l[lo:hi+1])
            
            if res != '':
                return res

    return ''

s = input()

l = ['vacancy', 'vacancies', 'opening', 'openings', 'post', 'posts', 'opportunity', 'opportunities', 'position', 'positions']
d = {}
for x in l:
    d[x] = 1

resVac = getVacancy(s, d)
if resVac == '':
    print("Vacancy information not found")
else:
    print(resVac)