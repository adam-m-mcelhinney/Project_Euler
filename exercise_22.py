# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
# first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

filePath = '/Users/amcelhinney/repos/Project_Euler/p022_names.txt'

with open(filePath) as f:
    names = f.readlines()


names = names[0].split(',')
names = [name.strip("'").strip('"').lower() for name in names]
names = sorted(names)



nameVals = [chr(96+i) for i in range(1,27)]
nameDict = dict(zip(nameVals, range(1, 27)))

def calcOneNameScore(name, rnk):
    score = 0
    for i in name:
        v = nameDict[i]
        score += v
    return score * rnk

i = 1
score = 0
for name in names:
    s = calcOneNameScore(name, rnk=i)
    score += s
    if i == 938:
        print(name, s, score)
    i += 1






assert(calcOneNameScore('colin', 938) == 49714)