import sys
import listsearch
sys.path.append(r"C:\DevLcl\Sandbox\python-sandbox\think_python\chapter_10")

fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\chapter_9\words.txt')

def word_list():
    thelist = []
    for line in fin:
        thelist.append(line.strip())
    return thelist


def find_reverse_pair(mylist, word):
    res = word[::-1]
    if (listsearch.search_in_list(mylist, res)):
        print(word, res)


mylist = word_list()
mylist.sort()

for word in mylist:
    find_reverse_pair(mylist, word)