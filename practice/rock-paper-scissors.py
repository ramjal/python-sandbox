from random import randint
p1Mark = 0
p2Mark = 0


def findWinner(p1, p2):
    if p1 == p2:
        return
    if p1 == 'r' and p2 == 'p':
        return 'p2'
    elif p1 == 'r' and p2 == 's':
        return 'p1'
    elif p1 == 'p' and p2 == 'r':
        return 'p1'
    elif p1 == 'p' and p2 == 's':
        return 'p2'
    elif p1 == 's' and p2 == 'r':
        return 'p2'
    elif p1 == 's' and p2 == 'p':
        return 'p1'    


def getRandomRockPaperScissors():
    n = randint(0, 2)
    if (n == 0):
        return 'r'
    if (n == 1):
        return 'p'
    else:
        return 's'
    

def play(uInput):
    global p1Mark
    global p2Mark
    if uInput in ['r','p','s']:
        p2 = getRandomRockPaperScissors()
        w = findWinner(uInput, p2)
        if w == 'p1':
            p1Mark += 1
        elif w == 'p2':
            p2Mark += 1
        print('{0} vs {1} - ({2} to {3})'.format(uInput, p2, p1Mark, p2Mark))
    else:
        print('*** Wrong input! ***')



if __name__ == "__main__":
    print('**** Rock Paper Scissors ****')
    print('r = Rock')
    print('p = Paper')
    print('s = Scissors')
    print("Enter 'q' to exit the game")

    while True:
        uInput = input()
        if uInput == 'q':
            break
        else:
            play(uInput)

