
fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\words.txt')

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True

#print(uses_all('ramin', 'rmniaramin'))
#print(uses_all('hoecdalfalfa', 'acefhlo'))

def check4uses_all(letters):
    counter = 0
    for line in fin:
        if uses_all(line.strip(), letters):
            counter += 1
    return counter

print(check4uses_all('aeiou'))
print(check4uses_all('aeiouy'))