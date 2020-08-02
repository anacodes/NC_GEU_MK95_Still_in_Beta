def chkDate(s, c):
    date = ""
    for x in s:
        if x == c or x.isdigit():
            date += x
            
    count = date.count(c)
    if count != 2:
        return ''
    
    slashIndex = date.find(c)
    if slashIndex+2 < len(date) and date[slashIndex+2] == c :
        return date

    if slashIndex+3 < len(date) and date[slashIndex+3] == c :
        return date
    
    return ''


def getD(s):
    for i in range(len(s)):
        if s[i] == '/' or s[i] == '-':
            l = max(0, i - 5)
            r = min(len(s) - 1, i + 10)
            res = chkDate(s[l:r+1], s[i])

            if res != '':
                return res
            
    return ''

def getDate(s):
    resDate = getD(s)
    return resDate