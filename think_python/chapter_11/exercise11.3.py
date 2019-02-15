found = dict()
def ackermann(m, n):
    if [m,n] in found:  #Error: unhashable type: 'list'
        return found[[m,n]]

    if m == 0:
        ret = n + 1
    elif m > 0 and n == 0:
        ret = ackermann(m-1, 1)
    elif m > 0 and n > 0:
        ret = ackermann(m-1, ackermann(m, n-1))
    
    found[[m,n]] = ret
    return ret



#print(ackermann(5, 6)) # RecursionError: maximum recursion depth exceeded in comparison
print(ackermann(3, 6))