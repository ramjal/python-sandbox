tries = 0

def findNumber(start, end):
    global tries
    tries += 1
    n = int((end - start) / 2)
    ret = input('The number is '.format(n))
    if ret == 'low':
        findNumber(n, end)
    elif ret == 'high':
        findNumber(start, n)
    elif ret == 'correct':
        print('Number of tries: '.format(tries))


findNumber(0, 100)
