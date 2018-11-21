def sumall(*args):
    e = 0
    for i in range(len(args)):
        e += args[i]
    return e


print(sumall(1,2,3,4,5,6,7,8,9,10,11))