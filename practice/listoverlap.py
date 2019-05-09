# Find all the numbers that list 'a' and 'b' share
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l = []

for i in a:
    if i in b and i not in l:
        l.append(i)

print(l)

# Doing the same thing in one line
print(set([x for x in a if x in b]))

