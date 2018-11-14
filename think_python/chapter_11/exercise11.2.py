
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


dic = {'a':1,'b':2,'c':2,'d':2,'e':3,'f':3,'g':4}

rev = invert_dict(dic)

print(dic)
print(rev)