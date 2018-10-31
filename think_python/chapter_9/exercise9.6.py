
fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\chapter_9\words.txt')

def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True

def check4abecedarian():
    counter = 0
    for line in fin:
        if is_abecedarian(line.strip()):
            counter += 1
    return counter

print(check4abecedarian())