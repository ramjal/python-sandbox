import random

"""
    Play the game
"""
def playGame(myNumber, inputNumber):
    bulls = 0
    cows = 0
    if inputNumber < 1000 or inputNumber > 9999:
        print("*** Enter only 4 digits! ***")
    else:
        myStr = str(myNumber)
        guessedStr = str(inputNumber)        

        for n in myStr:
            for m in guessedStr:
                if n == m:
                    cows += 1
                    break                

        for i in range(4):
            if myStr[i] == guessedStr[i]:
                bulls += 1
                cows -= 1
        if bulls == 4:
            print('********* Congratulations! YOU WON! The secret number was {} *********'.format(myNumber))
            return
        else:
            print('\t{} Bulls and {} Cows'.format(bulls, cows))


"""
    Make a 4 digits random number
"""
def getRandomNumber():
    n = '0132' # just to start from somewhere
    while True:
        n = random.sample('0123456789', 4)
        if n[0] != '0':
            break
    return int(''.join(n))


""" 
    Main function
"""
if __name__ == "__main__":
    print("Guess a 4 digit number. To quit the game enter 'q'. To see the secret number enter 's'.")
    myNumber = getRandomNumber()
    while True:
        inputData = input()
        if inputData == 'q':
            break
        elif inputData == 's':
            print(myNumber)
            break
        else:
            playGame(myNumber, int(inputData))
