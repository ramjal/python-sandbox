def getFibonacciList(n):
    l = [1,1]
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:         
        for i in range(2, n):
            l.append(l[i-2] + l[i-1])
        return l


try:
    n = int(input("How many Fibonacci numbers you need?\n"))
    print(getFibonacciList(n)) 
except Exception as err:
    print('There was an error: {0}'.format(err))