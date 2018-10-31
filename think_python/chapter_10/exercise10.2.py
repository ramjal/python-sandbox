def cumsum(myList):
    ret = []
    for i in range(1, len(myList)):
        ret.append(sum(myList[:i]))
    return ret


theList = [1, 2, 3, 4, 5, 6, 7 ,8 , 9]

print(cumsum(theList))

