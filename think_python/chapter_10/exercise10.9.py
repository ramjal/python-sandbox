fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\chapter_9\words.txt')

def word_list1():
    thelist = []
    for line in fin:
        thelist.append(line.strip())
    print(len(thelist))


def word_list2():
    thelist = []
    for line in fin:
        thelist = thelist + [line.strip()]
    print(len(thelist))

word_list1()
#word_list2()
