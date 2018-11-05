import sys
import listsearch
sys.path.append(r"C:\DevLcl\Sandbox\python-sandbox\think_python\chapter_10")

fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\chapter_9\words.txt')

def word_list():
    thelist = []
    for line in fin:
        thelist.append(line.strip())
    return thelist


def find_interlocks(mylist, word):
    w1 = word[::2]
    w2 = word[1::2]
    if listsearch.search_in_list(mylist, w1) and listsearch.search_in_list(mylist, w2):
        print(word, w1, w2)


mylist = word_list()
mylist.sort()

for word in mylist:
    find_interlocks(mylist, word)