def chkSalary(s, d):
    salary = ''
    
    l = ['rs.', 'rs', '₹', '$', 'lpa', 'ctc', 'lpa.', 'ctc.']
    no = {}
    for x in l:
        no[x] = 1
    
    for i in range(len(s)):
        if s[i] in d:
            if s[i] not in no:
                salary += s[i] + ' '

        elif s[i][0:-1] in d:
            if s[i][0:-1] not in no:
                salary += s[i][0:-1] + ' '
                
        elif s[i].isdigit():
            salary += s[i] + ' '
            
        elif s[i] == '-':
            if len(salary) > 0:
                salary += s[i] + ' '

    #Need to add cases where word ends with '.', ',', '-' and handle some ranges better
                    
    return salary[0:-1]

def getSalary(s, d):
    s = s.lower()
    l = s.split()
    
    for i in range(len(l)):
        if l[i] in d or l[i][0:-1] in d:
            lo = max(0, i - 5)
            hi = min(len(l) - 1, i + 5)
            return chkSalary(l[lo:hi+1], d)
            
    return ''
    

l = ['rs.', 'rs', '₹', '$', 'lakh', 'crore', 'thousand', 'lakhs', 'crores', 'thousands', 'lpa', 'ctc']

d = {}
for x in l:
    d[x] = 1

s = input()
resSalary = getSalary(s, d)

if resSalary == '' or resSalary in d:
    print('No salary found mentioned in the job description')
else:
    print(resSalary)
