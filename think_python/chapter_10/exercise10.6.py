def is_anagram(w1, w2):
    l1 = list(w1)
    l1.sort()
    l2 = list(w2)
    l2.sort()
    return l1 == l2


print(is_anagram('abc', 'cba'))