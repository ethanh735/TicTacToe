import turtle
from random import randint
import classes


def initBoard(size):
    board = [[] for i in range(size)]
    for rows in range(size):
        for cols in range(size):
            board[rows].append(0)
    return board


# TODO: regulate board size scale to current screen size
def drawBoard(t, board):
    # setup
    # scaling equation is currently arbitrary, tie to screen size
    scale = -20 * board.__len__() + 300
    t.tracer(0)
    t.pensize(4)
    t.color("black")
    x = y = -scale * (board.__len__() / 2)
    t.penup()
    t.setpos(x, y)
    t.pendown()

    # does this really need to be N^3
    for line in board:
        for tile in line:
            for i in range(4):
                t.forward(scale)
                t.left(90)
            x += scale
            t.penup()
            t.setpos(x, y)
            t.pendown()
        x -= scale * board.__len__()
        y += scale
        t.penup()
        t.setpos(x, y)
        t.pendown()


# TODO: handle strings that aren't num, num
def terminalPlace(player):
    # First input
    x = y = -1
    i = input()
    if i == "end" or i == "quit" or i == "stop":
        return True
    elif 3 <= i.__len__() <= 6:
        x, y = i.split(",")
        x = int(x)
        y = int(y)

    # Conditions for valid placement: if invalid, must enter input again
    while not (boardSize >= x >= 0 == logicBoard[x - 1][y - 1] and boardSize >= y >= 0):
        print("Invalid placement, enter another coordinate:")
        x = y = -1
        i = input()
        if i == "end" or i == "quit" or i == "stop":
            return True
        elif 3 <= i.__len__() <= 6:
            x, y = i.split(",")
            x = int(x)
            y = int(y)

    player.place(logicBoard, x, y)
    # logicBoard[x - 1][y - 1] = player
    return False


if __name__ == '__main__':

    # Board creation
    boardSize = 3
    logicBoard = initBoard(boardSize)
    drawBoard(turtle, logicBoard)

    # Selecting game mode
    gameMode = int(input("Press 1 to play against the computer, or 2 to play against another person locally: "))
    while gameMode < 1 or gameMode > 2:
        gameMode = int(input("Invalid game mode, enter a valid option: "))
    first = randint(0, 1)

    # Computer
    if gameMode == 1:
        print("Playing against the computer.")
        if first == 0:
            print("You go first!")
        else:
            print("The computer goes first!")

    # Local play
    elif gameMode == 2:
        print(f"Playing against someone locally.\nPlayer {first + 1} goes first!")

    # Gameplay loop
    gameOver = False
    plays = 0

    while not gameOver:
        countForX = countForO = 0

        # # Computer
        # if first == 0 and gameMode == 1:
        #     first = not first
        #
        # elif first == 1 and gameMode == 1:
        #     first = not first

        # Local Play
        if first == 0 and gameMode == 2:
            plays += 1
            # first player X: wherever click is, place an X on the board
            print(f"X's turn! Enter coordinates between 1,1 and {boardSize},{boardSize}:")
            gameOver = terminalPlace(classes.X())

            # if piece in first row, check below
            for col in range(boardSize):
                if isinstance(logicBoard[0][col], classes.X):
                    countForX = 1
                    # Checking below for consecutive pieces
                    for row in range(boardSize - 1):
                        if isinstance(logicBoard[row + 1][col], classes.X):
                            countForX += 1

            # if in first column of other rows, check right
            for row in range(boardSize):
                if isinstance(logicBoard[row][0], classes.X):
                    countForX = 1
                    # Checking right for consecutive pieces
                    for col in range(boardSize - 1):
                        if isinstance(logicBoard[row][col + 1], classes.X):
                            countForX += 1

            first = not first

        elif first == 1 and gameMode == 2:
            plays += 1
            # second player O: wherever click place O on board
            print(f"O's turn! Enter coordinates between 1,1 and {boardSize},{boardSize}:")
            gameOver = terminalPlace(classes.O())

            # if piece in first row, check below
            for col in range(boardSize):
                if isinstance(logicBoard[0][col], classes.O):
                    countForO = 1
                    # Checking below for consecutive pieces
                    for row in range(boardSize - 1):
                        if isinstance(logicBoard[row + 1][col], classes.O):
                            countForO += 1

            # if in first column of other rows, check right
            for row in range(boardSize):
                if isinstance(logicBoard[row][0], classes.O):
                    countForO = 1
                    # Checking right for consecutive pieces
                    for col in range(boardSize - 1):
                        if isinstance(logicBoard[row][col + 1], classes.O):
                            countForO += 1

            first = not first

        # Terminal board representation
        for row in range(boardSize):
            print(logicBoard[row])

        # Win condition
        if countForX == boardSize:
            gameOver = True
            print("Game Over! X wins!")
        elif countForO == boardSize:
            gameOver = True
            print("Game Over! O wins!")
        elif plays == boardSize * boardSize:
            gameOver = True
            print("It's a draw!")

    # TODO: make quitting actually shut everything down
    turtle.done()
