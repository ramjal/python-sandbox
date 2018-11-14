# a simple version of fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



# a faster version by using dict
known = {0:0, 1:1}
def fibonacci2(n):
    if n in known:
        return known[n]

    res = fibonacci2(n - 1) + fibonacci2(n - 2)
    known[n] = res
    return res



print(fibonacci(32))
print(fibonacci2(32))
#print(known)

