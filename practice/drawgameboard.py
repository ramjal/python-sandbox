def printLines(n):
    line = ''
    for _ in range(n): #using _ instead of i removes the warring of 'unused variable'
        line += ' ---'
    line += ' '
    print(line)


def printPipes(n):
    pipe = '|'
    for _ in range(n): #using _ instead of i removes the warring of 'unused variable'
        pipe += '   |'
    print(pipe)


if __name__ == "__main__":
    n = int(input("What's the size of the board?"))
    for i in range(n):
        printLines(n)
        printPipes(n)
    printLines(n)