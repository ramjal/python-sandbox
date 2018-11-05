def has_duplicates(my_list):
    lcopy = my_list[:]
    lcopy.sort()
    for i in range(len(lcopy)-1):
        if lcopy[i] == lcopy[i+1]:
            return True
    return False

print(has_duplicates([1,2,3,4,5,6]))
print(has_duplicates([1,3,3,4,5,6]))
