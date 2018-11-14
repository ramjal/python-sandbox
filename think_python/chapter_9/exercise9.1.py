fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\words.txt')

counter = 0
for line in fin:
    theLine = line.strip()
    if len(theLine) > 20:
        print(theLine)
