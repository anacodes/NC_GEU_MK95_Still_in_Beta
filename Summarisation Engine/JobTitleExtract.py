def getTitle(s, d):
    word_cnt = {}
    for x in s:
        if x[-1] == '.' or x[-1] == ',':
            x = x[0:-1]
        
        if x not in word_cnt:
            word_cnt[x] = 0
        word_cnt[x] += 1

    
    JobTitle = ''
    max_score = 0
    for title in d:
        curr_score = 0
        titleX = title.split()
        
        for word in titleX:
            word = word.lower()
            if word in word_cnt:
                curr_score += word_cnt[word]
            else:
                curr_score -= 1
            
        if curr_score > max_score:
            max_score = curr_score
            JobTitle = title

    return JobTitle



d = {}

# Reading all prominent job titles
with open('Job_Title.txt', 'r') as file:
    Lines = file.readlines()
    for line in Lines:
        line = line[0:-1]
        d[line] = True
        

s = input()
s = s.lower()
l = s.split()
r = min(len(l), 20)
resTitle = getTitle(l[0:r], d)

if resTitle == '':
    print('No Title found')
else:
    print(resTitle)