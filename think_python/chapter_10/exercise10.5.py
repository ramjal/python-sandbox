def is_sorted(myList):
    copy = myList[:]
    copy.sort()
    if myList == copy:
        return True
    else:
        return False

theList = [1, 2, 3, 4, 5, 6, 7 ,8 , 9]

print(is_sorted(theList))

theList = [1, 2, 3, 4, 7, 8, 7 ,8 , 9]

print(is_sorted(theList))