fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\words.txt')

def getChars(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


anagDict = {}
for line in fin:
    word = line.strip().lower()
    chars = getChars(word)
    if chars in anagDict:
        anagDict[chars].append(word)
    else:
        anagDict[chars] = [word]


# Print all the anagram set not in order
# for w in anagDict:
#     if len(anagDict[w]) > 3:
#         print(anagDict[w])


def is_metathesis(w1, w2):
    l1 = list(w1)
    l2 = list(w2)
    for i in range(0, len(w1)):
        for j in range(i+1, len(w1)):
            lswap = l1.copy()
            lswap[i], lswap[j] = lswap[j], lswap[i]
            if lswap == l2:
                return True
    return False


def is_metathesis_new(w1, w2):
    assert len(w1) == len(w2)
    count = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            count += 1
    return (count == 2)


def print_metathesis(l):
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            if is_metathesis(l[i], l[j]):
                print(l[i], l[j])


for w in anagDict:
    if len(anagDict[w]) > 7:
        print(anagDict[w])
        print_metathesis(anagDict[w])


# print(is_metathesis('arinm', 'armin'))

# print(is_metathesis_new('speir', 'spire'))