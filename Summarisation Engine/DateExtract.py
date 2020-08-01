def chkDate(s):
    date = ""
    for x in s:
        if x == '/' or x.isdigit():
            date += x
            
    count = date.count('/')
    if count != 2:
        return ''
    
    slashIndex = date.find('/')
    if slashIndex+2 < len(date) and date[slashIndex+2] == '/' :
        return date

    if slashIndex+3 < len(date) and date[slashIndex+3] == '/' :
        return date
    
    return ''


def getDate(s):
    for i in range(len(s)):
        if s[i] == '/':
            l = max(0, i - 5)
            r = min(len(s) - 1, i + 10)
            res = chkDate(s[l:r+1])

            if res != '':
                return res
            
    return ''

s = input()
resDate = getDate(s)
if resDate == '':
    print('No Date found in the text')
else:
    print(resDate)