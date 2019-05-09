
def isPrime(theNumber):
    l = []
    for i in range(2, theNumber):
        if (theNumber % i == 0):
            l.append(i)
   
    if len(l) == 0:
        return True

    return False


try:
    n = int(input("Enter a number:\n"))
    if isPrime(n):
        print("{} is a prime number".format(n))
    else:
        print("{} is NOT a prime number".format(n))
except Exception as err:
    print('There was an error: {0}'.format(err))