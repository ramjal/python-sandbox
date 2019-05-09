try:
    theNumber = int(input('Give me a number\n'))
    print('Divisors of {0} are the followings:'.format(theNumber))
    for i in range(2, theNumber):
        if (theNumber % i == 0):
            print(i)

except Exception as err:
    print("Something went wrong: {0}".format(err))