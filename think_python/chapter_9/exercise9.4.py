
fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\chapter_9\words.txt')

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

print(uses_only('ramin', 'rmniaramin'))
print(uses_only('hoealfalfa', 'acefhlo'))