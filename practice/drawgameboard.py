
def printLines(n):
    line = ''
    for i in range(n):
        line += ' ---'
    line += ' '
    print(line)

def printPipes(n):
    pipe = '|'
    for i in range(n):
        pipe += '   |'
    print(pipe)


if __name__ == "__main__":
    n = int(input("What's the size of the board?"))
    for i in range(n):
        printLines(n)
        printPipes(n)
    printLines(n)