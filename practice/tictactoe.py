def drawBoard(game):
    line = ' --- --- --- '
    print(line)
    print('| {0} | {1} | {2} |'.format(game[0][0], game[0][1], game[0][2]))
    print(line)
    print('| {0} | {1} | {2} |'.format(game[1][0], game[1][1], game[1][2]))
    print(line)
    print('| {0} | {1} | {2} |'.format(game[2][0], game[2][1], game[2][2]))
    print(line)


# findout who is the winner in tic tac toe
def checkTheResult(game):
    (winner, w) = checkDiagonal1(game, len(game))
    if winner:
        #print('The winner is {}'.format(w))
        return w
    (winner, w) = checkDiagonal2(game, len(game))
    if winner:
        #print('The winner is {}'.format(w))
        return w
    (winner, w) = checkHorizontalAll(game, len(game))
    if winner:
        #print('The winner is {}'.format(w))
        return w
    (winner, w) = checkVerticalAll(game, len(game))
    if winner:
        #print('The winner is {}'.format(w))
        return w

    return False


# horizontal
def checkHorizontalAll(game, l):
    for row in range(0, l):
        (winner, w) = checkHorizontal(game, l, row)
        if winner:
            return (winner, w)
    return (False, 0)


# horizontal
def checkHorizontal(game, l, row):
    for i in range(1, l):
        if game[row][0] != game[row][i] or game[row][0] == ' ':
            return (False, 0)
    return (True, game[row][0])


# Vertical
def checkVerticalAll(game, l):
    for col in range(0, l):
        (winner, w) = checkVertical(game, l, col)
        if winner:
            return (winner, w)
    return (False, 0)


# Vertical
def checkVertical(game, l, col):
    for i in range(1, l):
        if game[0][col] != game[i][col] or game[0][col] == ' ':
            return (False, 0)
    return (True, game[0][col])


# diagonal left to right
def checkDiagonal1(game, l):
    for i in range(1, l):
        if game[0][0] != game[i][i] or game[0][0] == ' ':
            return (False, 0)
    return (True, game[0][0])


# diagonal right to left
def checkDiagonal2(game, l):
    for i in range(1, l):
        if game[0][l-1] != game[i][l-1-i] or game[0][l-1] == ' ':
            return (False, 0)
    return (True, game[0][l-1])


# check to see if any slot is left
def boardIsFull(game):
    l = len(game)
    for i in range(0, l):
        for j in range(0, l):
            if game[i][j] == ' ':
                return False
    return True


if __name__ == "__main__":
    game = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

    winner = ''
    currentPlayer = 'X'
    drawBoard(game)

    while True:
        (x,y) = input("Current player = {}\nWhat's your next move?\n".format(currentPlayer)).split(',')
        col = int(x) - 1
        row = int(y) - 1
        if col < 0 or row > 2:
            print("*** Not a valid move!")
        elif game[col][row] != ' ':
            print("*** Not a valid move! This slot is already taken.")
        else:
            game[col][row] = currentPlayer
            drawBoard(game)
            if currentPlayer == 'X':
                currentPlayer = 'O'
            else:
                currentPlayer = 'X'

        winner = checkTheResult(game)
        if winner:
            print("*** Congratulations '{}' is the winner! ***".format(winner))
            break
        
        if boardIsFull(game):
            print("*** End of game! ***")
            break

