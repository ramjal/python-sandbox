# rotate a char
def rotate_char2(c, rotation_amount):
    ord1 = ord(c)    
    
    if 65 <= ord1 <= 90: #upper case
        ord2 = ord(c) + rotation_amount
        if ord2 > 90:
            ord2 = 64 + ord2 - 90
        if ord2 < 65:
            ord2 = 91 - (65 - ord2)
    elif 97 <= ord1 <= 122: #lower case:     
        ord2 = ord(c) + rotation_amount
        if ord2 > 122:
            ord2 = 96 + ord2 - 122
        if ord2 < 97:
            ord2 = 123 - (97 - ord2)
    else:
        ord2 = 63 #error ?

    return chr(ord2)


# rotate a char
def rotate_char(letter, rotAmount):
    if letter.isupper():
        base = ord('A')
    elif letter.islower():
        base = ord('a')
    else:
        return letter

    index = ord(letter) - base
    newOrd = (index + rotAmount) % 26 + base
    return chr(newOrd)    

# rotate a word
def rotate_word(word, rotAmount):
    rotated = ''
    for letter in word:
        rotated += rotate_char(letter, rotAmount)
    return rotated


def rotate13_sentence(sentece):
    for word in sentece.split():
        print(rotate_word(word, 13))


# print('cheer', rotate_word('cheer', 7))
# print('melon', rotate_word('melon', -10))
# print('sleep', rotate_word('sleep', 9))
# print('gurer', rotate_word('gurer', 13))


rotate13_sentence('Uv gurer. Guvf vf abg ernyyl wbxr. Whfg univat fbzr sha jvgu gubfr')
rotate13_sentence('jub pna\'g ebg13 na negvpyr')
rotate13_sentence('Gb or ernyyl zrna, sbyybj-hc gb guvf negvpyr jvgu fbzrguvat yvxr')
rotate13_sentence('Obl, gung jnf gur shaavrfg wbxr V rire urneq')