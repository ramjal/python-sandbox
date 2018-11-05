def is_anagram(w1, w2):
    l1 = list(w1)
    l1.sort()
    l2 = list(w2)
    l2.sort()
    return l1 == l2


while True:
    words = input('Give me two words (space delimited)...\n')
    if words == 'exit':
        break

    if len(words.split()) != 2:
        print('not a good entry! try again!')
        
    if is_anagram(words.split()[0], words.split()[1]):
        print('anagram')
    else:
        print('no-anagram')

# print(is_anagram('abc', 'cba'))