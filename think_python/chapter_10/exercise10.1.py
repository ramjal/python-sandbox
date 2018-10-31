
def nested_sum(myList, mySum=0):
    for item in myList:
        if type(item) is int:
            mySum += item
        elif type(item) is list:
            mySum = nested_sum(item, mySum)

    return mySum



theList = [1, 2, 3, [1, 2, 3], 'test', 4, 5, [6, [1, 2, 3, [1, 2]], 7], 8]

print(nested_sum(theList))

