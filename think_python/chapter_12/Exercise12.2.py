fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\words.txt')

"""
worldDict = {}
worldList = []
anagramSet = []

def populate_dict():    
    for line in fin:
        worldDict[line.strip()] = len(line.strip())


def is_anagram(w1, w2):
    l1 = list(w1)
    l1.sort()
    l2 = list(w2)
    l2.sort()
    return l1 == l2


def populate_list(n):
    for w in worldDict:
        if worldDict[w] == n:
            worldList.append(w)


populate_dict()
populate_list(8)

for i in range(0, len(worldList)):
    anagramSet.clear()
    anagramSet.append(worldList[i])
    for j in range(i+1, len(worldList)):
        if is_anagram(worldList[i], worldList[j]):
            anagramSet.append(worldList[j])
    
    if len(anagramSet) > 1:
        print(anagramSet) 
"""

def getChars(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


anagDict = {}
for line in fin:
    word = line.strip().lower()
#     if len(word) != 8: # What collection of 8 letters forms the most possible bingos? Hint: there are seven.
#         continue
    chars = getChars(word)
    if chars in anagDict:
        anagDict[chars].append(word)
    else:
        anagDict[chars] = [word]

# Print all the anagram set not in order
# for w in anagDict:
#     if len(anagDict[w]) > 3:
#         print(anagDict[w])

# Modify the previous program so that it prints the longest list of anagrams first, followed by
# the second longest, and so on.

# Print all the anagram set in order
l = []
for w in anagDict:
    if len(anagDict[w]) > 3:
        l.append((len(anagDict[w]), anagDict[w]))

l.sort(reverse=True)
for e in l:
      print(e)  
#     print(e[1])

