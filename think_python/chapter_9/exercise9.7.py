fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\words.txt')

def is_three_consecutive_double2(word):
    for i in range(len(word)-1):
        if len(word[i+1:i+6:2]) < 3:
            return False
        if word[i:i+5:2] == word[i+1:i+6:2]:
            return True
    return False


def is_three_consecutive_double(word):
    if len(word) < 6:
        return False
    for i in range(len(word)-5):
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            return True
    return False


def check4abecedarian():
    for line in fin:
        word = line.strip()
        if is_three_consecutive_double2(word):
            print(word)


# is_three_consecutive_double2('bookkeeper')
check4abecedarian()