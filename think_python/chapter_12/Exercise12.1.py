# Write a function called most_frequent that takes a string and prints the letters
# in decreasing order of frequency.

def most_frequent(s):
    d = dict()
    for c in s:
        d[c] = d.setdefault(c, 0) + 1
    
    pairs = zip(d.values(), d.keys()) # Could be included in-line in the next line
    for v in sorted(pairs, reverse=True):
        print(v)


most_frequent('There are three ways to count letter \
                frequency that result in very different \
                charts for common letters. The first method, \
                used in the chart below, is to count letter \
                frequency in root words of a dictionary'.replace(" ", ""))