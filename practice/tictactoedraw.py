
def drawBoard(game):
    line = ' --- --- --- '
    print(line)
    print('| {0} | {1} | {2} |'.format(game[0][0], game[0][1], game[0][2]))
    print(line)
    print('| {0} | {1} | {2} |'.format(game[1][0], game[1][1], game[1][2]))
    print(line)
    print('| {0} | {1} | {2} |'.format(game[2][0], game[2][1], game[2][2]))
    print(line)
    

if __name__ == "__main__":
    game = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

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

