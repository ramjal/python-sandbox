def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif (first(word) == last(word)):
        return is_palindrome(middle(word))
    else:
        return False


#print('Give me a word')
w = input('Give me a word to check for Palindrome\n')
print(is_palindrome(w))