def is_palindrome(word):
    return (word[::] == word[::-1])


while True:
    w = input('Give me a word to check for Palindrome\n')
    if w == 'exit':
        break
    print(is_palindrome(w))

