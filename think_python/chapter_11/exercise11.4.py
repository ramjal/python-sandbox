def has_duplicates(my_list):
    myDict = {}
    for e in my_list:
        if e in myDict:
            return True
        else:
            myDict[e] = True
            
    return False

print(has_duplicates([1,2,3,4,5,6]))
print(has_duplicates([1,3,3,4,5,6]))
