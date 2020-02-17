import random

# Read the file into a list
def getRandomWord():
    fname = r'C:\DevLcl\Sandbox\python_sandbox\practice\sowpods.txt'
    with open(fname) as fp:
        lines = fp.read().splitlines()
    return(random.choice(lines))


# Print the word with guessed letters
def printWord(word, guessedOK):
    guessedSoFar = ''
    for l in word:
        if l in guessedOK:
            guessedSoFar += l
        else:
            guessedSoFar += '_'
    print(guessedSoFar)


if __name__ == "__main__":
    guessedOK = set()
    word = getRandomWord()
    print("Welcome to Hagman!")
    while True:
        letter = input("Guess your letter: ").upper()
        if len(letter) != 1:
            print("Enter only one letter!")
        elif letter in guessedOK:
            print("Letter already guessed!")
        elif letter in word:            
            guessedOK.add(letter.upper())
            printWord(word, guessedOK)
            print("Good")
        else:
            print("Bad")
