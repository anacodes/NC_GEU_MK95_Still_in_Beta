def chkSalary(s, d):
    salary = ''
    
    l = ['rs.', 'rs', '₹', '$', 'lpa', 'ctc', 'lpa.', 'ctc.']
    no = {}
    for x in l:
        no[x] = 1
    
    for i in range(len(s)):
        if s[i][-1] == '.':
            s[i] = s[i][0:-1]

        if s[i] in d:
            if s[i] not in no:
                salary += s[i] + ' '
                
        elif s[i].isdigit():
            salary += s[i] + ' '

        elif s[i].find('.') != -1 and s[i].find('.') != 0:
            ok = True
            for x in s[i]:
                if x.isdigit() == False and x != '.':
                    ok = False
                    
            if ok:
                salary += s[i] + ' '

        elif s[i].find(',') != -1 and s[i].find(',') != 0:
            ok = True
            for x in s[i]:
                if x.isdigit() == False and x != ',':
                    ok = False
                    
            if ok:
                salary += s[i] + ' '

        elif s[i].find('-') != -1 and s[i].find('-') != 0:
            ok = True
            for x in s[i]:
                if x.isdigit() == False and x != '-':
                    ok = False
                    
            if ok:
                salary += s[i] + ' '
            
        elif s[i] == '-':
            if len(salary) > 0:
                salary += s[i] + ' '

    # Need to add cases where there are no spaces present between like, Rs.xxx, Rs. xxx-yyy            
    return salary[0:-1]

def getSal(s, d):
    s = s.lower()
    l = s.split()
    
    confirm = ['lakh', 'lac', 'crore', 'thousand', 'lakhs', 'lacs', 'crores', 'thousands']
    confirm_list = {}

    for x in confirm:
        confirm_list[x] = True

    for i in range(len(l)):
        if l[i] in confirm_list or l[i][0:-1] in confirm_list:
            lo = max(0, i - 3)
            return chkSalary(l[lo:i+1], d)

    for i in range(len(l)):
        if l[i] in d or l[i][0:-1] in d:
            lo = max(0, i - 5)
            hi = min(len(l) - 1, i + 5)
            return chkSalary(l[lo:hi+1], d)
            
    return ''
    
def getSalary(s):
    l = ['rs.', 'rs', '₹', '$', 'lakh', 'lac', 'crore', 'thousand', 'lakhs', 'lacs', 'crores', 'thousands', 'lpa', 'ctc']

    d = {}
    for x in l:
        d[x] = True

    resSalary = getSal(s, d)
    return resSalary