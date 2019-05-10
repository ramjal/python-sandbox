# findout who is the winner in tic tac toe
def checkTheResult():
    game = [[1, 2, 1, 2],
            [2, 1, 1, 2],
            [2, 2, 1, 2],
            [2, 1, 0, 0]]
    (winner, w) = checkDiagonal1(game, len(game))
    if winner:
        print('The winner is {}'.format(w))
        return
    (winner, w) = checkDiagonal2(game, len(game))
    if winner:
        print('The winner is {}'.format(w))
        return
    (winner, w) = checkHorizontalAll(game, len(game))
    if winner:
        print('The winner is {}'.format(w))
        return
    (winner, w) = checkVerticalAll(game, len(game))
    if winner:
        print('The winner is {}'.format(w))
        return
    print('There is no winner')


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
        if game[row][0] != game[row][i]:
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
        if game[0][col] != game[i][col]:
            return (False, 0)
    return (True, game[0][col])


# diagonal left to right
def checkDiagonal1(game, l):
    for i in range(1, l):
        if game[0][0] != game[i][i]:
            return (False, 0)
    return (True, game[0][0])


# diagonal right to left
def checkDiagonal2(game, l):
    for i in range(1, l):
        if game[0][l-1] != game[i][l-1-i]:
            return (False, 0)
    return (True, game[0][l-1])


if __name__ == "__main__":
    checkTheResult()
