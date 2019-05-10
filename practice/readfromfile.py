import os

#fileName = 'C:\\DevLcl\\Sandbox\\python_sandbox\\practice\\nameslist.txt'
#fileName = r'C:\DevLcl\Sandbox\python_sandbox\practice\nameslist.txt'
fileName = os.path.join(os.getcwd(), 'nameslist.txt')
names = {}

with open(fileName, 'r') as open_file:
    while True:
        line = open_file.readline().rstrip('\n')
        if line:
            names[line] = names.setdefault(line, 0) + 1
        else:
             break

print(names)

