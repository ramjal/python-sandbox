def rev_str(theStr):
    l = len(theStr)
    for i in range(l - 1, -1, -1):
        yield theStr[i]


# Using for loop
for s in rev_str('Ramin'):
    print(s) 
