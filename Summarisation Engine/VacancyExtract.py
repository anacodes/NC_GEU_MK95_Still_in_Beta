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


    # To handle cases like xxxx - yyyy
    for i in range(len(s)):       
        if s[i] == '-':
            if i > 0 and i + 1 < len(s):
                prev = s[i - 1]
                nxt = s[i + 1]

                if nxt[-1] == '.' or nxt[-1] == ',':
                    nxt = nxt[0:-1]

                if prev.isdigit() and nxt.isdigit():
                    return prev + '-' + nxt   


    ## Remaining cases to handle :-
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