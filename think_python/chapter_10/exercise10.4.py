def chop(myList):
    del myList[0]
    del myList[-1]

theList = [1, 2, 3, 4, 5, 6, 7 ,8 , 9]

chop(theList)
print(theList)


