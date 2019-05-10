"""
    Write a function that takes an ordered list of numbers 
    (a list where the elements are in order from smallest to largest) and another number. 
    The function decides whether or not the given number is inside the list and returns 
"""
counter = 0

def doBinarySearch(l, n):
    global counter
    counter += 1
    if len(l) == 1:
        return l[0] == n
    middle = int(len(l) / 2)
    if n == l[middle]:
        return True
    elif n > l[middle]:
        return doBinarySearch(l[middle:], n)
    else:
        return doBinarySearch(l[0: middle], n)


if __name__ == "__main__":    
    l = [1, 3, 5, 9, 24, 30, 42, 43, 241, 389, 420, 483, 500]    
    print('{0} - in {1} times'.format(doBinarySearch(l, 34), counter))
    print('{0} - in {1} times'.format(doBinarySearch(l, 389), counter))

