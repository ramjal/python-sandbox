
fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\words.txt')

def avoids(word, forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True

print(avoids('ramin', 'sdfccgvx'))
print(avoids('ramin', 'sdfccgvmx'))