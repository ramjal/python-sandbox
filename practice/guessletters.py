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
    print("Welcome to Hagman!")
    word = "RAMIN RASOULI"
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
