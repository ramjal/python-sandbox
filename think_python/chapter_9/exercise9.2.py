
fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\chapter_9\words.txt')

def has_no_e(word):
    return word.find('e') == -1

def check4e():
    counter = 0
    no_e_counter = 0
    for line in fin:
        counter += 1
        theLine = line.strip()
        if has_no_e(theLine):
            print(theLine)
            no_e_counter += 1
    return no_e_counter * 100 // counter
    

#print(has_no_e('raminde'))
print('Percent: %', check4e())