import sys
import listsearch
sys.path.append(r"C:\DevLcl\Sandbox\python-sandbox\think_python\chapter_10")

fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\words.txt')

def word_list():
    thelist = []
    for line in fin:
        thelist.append(line.strip())
    return thelist


def find_interlocks2(mylist, word):
    w1 = word[::2]
    w2 = word[1::2]
    if listsearch.search_in_list(mylist, w1) and listsearch.search_in_list(mylist, w2):
        print(word, w1, w2)


def find_interlocks3(mylist, word):
    w1 = word[::3]
    w2 = word[1::3]
    w3 = word[2::3]
    if listsearch.search_in_list(mylist, w1) \
        and listsearch.search_in_list(mylist, w2) \
        and listsearch.search_in_list(mylist, w3):
        print(word, w1, w2, w3)


def interlocks2():
    mylist = word_list()
    mylist.sort()
    for word in mylist:
        find_interlocks2(mylist, word)


def interlocks3():
    mylist = word_list()
    mylist.sort()
    for word in mylist:
        find_interlocks3(mylist, word)


interlocks3()
