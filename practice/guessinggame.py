tries = 0

def findNumber(start, end):
    global tries
    tries += 1
    n = int((start + end) / 2)
    ret = input('The number is {}\n'.format(n))
    if ret == 'low':
        findNumber(n, end)
    elif ret == 'high':
        findNumber(start, n)
    elif ret == 'yes':
        print('Number of tries: {}\n'.format(tries))


findNumber(0, 100)
