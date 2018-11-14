fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\words.txt')

def word_list():
    thelist = []
    for line in fin:
        thelist.append(line.strip())
    return thelist


def in_bisect(thelist, word, counter):
    counter[0] = counter[0] + 1
    if len(thelist) == 0:
        return False
    if len(thelist) == 1:
        if word == thelist[0]:
            return True
        else:
            return False

    mid = len(thelist) // 2
    if word >= thelist[mid]:
        thelist = thelist[mid:]
    else:
        thelist = thelist[:mid]

    return in_bisect(thelist, word, counter)


mylist = word_list()
mylist.sort()
# mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# mylist = [1,2,3]
counter = [0]
print(in_bisect(mylist, 'test=ing', counter))
print('%d times' % counter[0])
