import sys
import turtle
from os import system, name
from random import randint

import classes


def initBoard(size):
    # List of lists
    board = [[] for i in range(size)]
    for rows in range(size):
        for cols in range(size):
            board[rows].append('-')
    return board


def drawBoard(t, bSize, sSize):
    # setup
    scale = sSize[0] / bSize
    x = y = -scale * (bSize / 2)
    t.tracer(2, 0)
    t.pensize(15 / bSize)
    t.hideturtle()
    t.penup()
    t.setpos(x, y + scale)
    t.pendown()

    # Drawing horizontal lines
    y += scale
    for i in range(bSize - 1):
        t.forward(sSize[0])
        y += scale
        t.penup()
        t.setpos(x, y)
        t.pendown()

    x = y = -scale * (bSize / 2)
    t.penup()
    t.setpos(x + scale, y)
    t.pendown()

    # Drawing vertical lines
    x += scale
    for j in range(bSize - 1):
        t.setheading(90)
        t.forward(sSize[0])
        x += scale
        t.penup()
        t.setpos(x, y)
        t.pendown()


def getBoardSize():
    # can be any positive int between 1-100
    print("Enter Board Size: ", end='')
    while True:
        bs = input()
        try:
            bs = int(bs)
            if bs <= 0 or bs > 100:
                raise ValueError
        except ValueError:
            print("Invalid input. Enter Board Size: ", end='')
        else:
            break
    return bs


def getDisplayFormat():
    # 1 is graphic, 2 is text
    print("Press 1 to play on a graphical screen, or 2 to play a text-based game: ", end='')
    while True:
        df = input()
        if df == '1' or df == '2':
            break
        else:
            print("Invalid input.\nPress 1 to play on a graphical screen, or 2 to play a text-based game: ", end='')
    return int(df)


def getGameMode():
    # 1 is computer, 2 is local vs
    print("Press 1 to play against the computer, or 2 to play against another person locally: ", end='')
    while True:
        gm = input()
        if gm == '2':
            break
        else:
            print("Invalid input.\nPress 1 to play against the computer, or 2 to play against another person locally:", end='')
    return int(gm)


def terminalPlace(player):
    # Emulates a do-while loop
    while True:
        i = input()

        # Input handling
        if i == "end" or i == "quit" or i == "stop" or i == "exit" or i == "q" or i == "s" or i == "e":
            return True
        else:
            try:
                x, y = i.split(",")
                assert i.__len__() >= 3 or i.__len__() <= 7
            except ValueError or AssertionError:
                print(f"Invalid format, enter a valid coordinate as num,num:")
                continue
            else:
                x = int(x)
                y = int(y)

                # Valid placement conditions
                if 0 <= x <= boardSize and 0 <= y <= boardSize and logicBoard[x - 1][y - 1] == '-':
                    break
                print(f"Invalid placement, enter another coordinate between 1,1 and {boardSize},{boardSize}:")

    player.place(logicBoard, x, y)
    return False


def terminalRefresh():
    # terminal clearing based on OS type
    if name == 'nt':
        clear = system('cls')
    elif name == 'posix':
        clear = system('clear')
    for row in range(boardSize):
        print(logicBoard[row])


# TODO: dissolve so that over bool is the only thing checked (no game logic checking in loop)
def terminalWin(countX, countO, plays):
    # Win condition
    if countX == boardSize:
        print("Game Over! X wins!")
        return True
    elif countO == boardSize:
        print("Game Over! O wins!")
        return True
    elif plays == boardSize * boardSize:
        print("It's a draw!")
        return True
    return False


def graphicalPlace(x, y, bSize, sSize):
    return
    # # Emulates a do-while loop
    # while True:
    #     print("Which tile is the click in?")
    #     break
    #     # Figure out which spot the click coordinates are in
    #     # instance - 1 / boardSize:
    #     # Board of 4: between 1/6 and 2/6 screenSize, 2/6 and 3/6 screenSize, 3/6 and 4/6 screenSize, 4/6 and 5/6 screenSize


def computerGraphicalGame(over, first):
    return


def pvpGraphicalGame(over, first):
    plays = 0
    while not over:
        countX = countO = 0
        turtx = turtle.xcor()
        turty = turtle.ycor()

        if first == 0:
            plays += 1
            print("X's turn! click any valid spot on the board.")
            # Wait for a click to happen
            while turtx == turtle.xcor() and turty == turtle.ycor():
                turtle.onclick(turtle.goto)
                # graphicalPlace(turtle.xcor(), turtle.ycor(), boardSize, turtle.screensize())
                print(turtle.pos())

            first = not first
            over = terminalWin(countX, countO, plays)

        elif first == 1:
            plays += 1
            print("O's turn! click any valid spot on the board.")
            # Wait for a click to happen
            while turtx == turtle.xcor() and turty == turtle.ycor():
                turtle.onclick(turtle.goto)
                # graphicalPlace(turtle.xcor(), turtle.ycor(), boardSize, turtle.screensize())
                print(turtle.pos())

            first = not first
            over = terminalWin(countX, countO, plays)


def computerTerminalGame(over, first):
    return
    # plays = 0
    #
    # if first == 0:
    #     print("You go first!")
    # else:
    #     print("The computer goes first!")
    # while not over:
    #     countX = countO = 0
    #     if first == 0:
    #         first = not first
    #
    #     elif first == 1:
    #         first = not first

    #     # Terminal board representation
    #     for row in range(boardSize):
    #         print(logicBoard[row])
    #
    #     over = terminalWin(countX, countO, plays)


# TODO: improve win condition checking
def pvpTerminalGame(over, first):
    plays = 0
    while not over:
        countX = countO = 1

        if first == 0:
            plays += 1
            if plays == boardSize ** 2:
                print("It's a draw!")
                over = True
            # first player X: wherever coordinates are, place an X on the board
            print(f"X's turn! Enter coordinates between 1,1 and {boardSize},{boardSize}:")
            if terminalPlace(classes.X()):
                break

            # \ diagonal check
            if logicBoard[0][0] == 'X':
                for j in range(1, boardSize - 1):
                    if logicBoard[j][j] == 'X':
                        countX += 1
            if countX >= boardSize:
                print("Game Over! X wins!")
                over = True
            else:
                countX = 1

            # / diagonal check
            if logicBoard[0][boardSize - 1] == 'X':
                col = boardSize - 2
                for j in range(1, boardSize - 1):
                    if logicBoard[j][col] == 'X':
                        countX += 1
                    col -= 1
            if countX >= boardSize:
                print("Game Over! X wins!")
                over = True
            else:
                countX = 1

            for tile in range(boardSize - 1):
                # first row check for vertical win
                if logicBoard[0][tile] == 'X':
                    for j in range(boardSize - 1):
                        if logicBoard[j][tile] == 'X':
                            countX += 1
                if countX >= boardSize:
                    print("Game Over! X wins!")
                    over = True
                else:
                    countX = 1
                    
                # first column check for horizontal win
                if logicBoard[tile][0] == 'X':
                    for j in range(boardSize - 1):
                        if logicBoard[tile][j] == 'X':
                            countX += 1
                if countX >= boardSize:
                    print("Game Over! X wins!")
                    over = True
                else:
                    countX = 1
                
            first = not first
            terminalRefresh()

        elif first == 1:
            plays += 1
            if plays == boardSize ** 2:
                print("It's a draw!")
                over = True
            # second player O: wherever coordinates are, place O on board
            print(f"O's turn! Enter coordinates between 1,1 and {boardSize},{boardSize}:")
            if terminalPlace(classes.O()):
                break

            # \ diagonal check
            if logicBoard[0][0] == 'O':
                for j in range(1, boardSize - 1):
                    if logicBoard[j][j] == 'O':
                        countO += 1
            if countO >= boardSize:
                print("Game Over! O wins!")
                over = True
            else:
                countO = 1
                    
            # / diagonal check
            if logicBoard[0][boardSize - 1] == 'O':
                col = boardSize - 2
                for j in range(1, boardSize - 1):
                    if logicBoard[j][col] == 'O':
                        countO += 1
                    col -= 1
            if countO >= boardSize:
                print("Game Over! O wins!")
                over = True
            else:
                countO = 1

            for tile in range(boardSize - 1):
                # first row check for vertical win
                if logicBoard[0][tile] == 'O':
                    for j in range(boardSize - 1):
                        if logicBoard[j][tile] == 'O':
                            countO += 1
                if countO >= boardSize:
                    print("Game Over! O wins!")
                    over = True
                else:
                    countO = 1
                    
                # first column check for horizontal win
                if logicBoard[tile][0] == 'O':
                    for j in range(boardSize - 1):
                        if logicBoard[tile][j] == 'O':
                            countO += 1
                if countO >= boardSize:
                    print("Game Over! O wins!")
                    over = True
                else:
                    countO = 1
                                
            first = not first
            terminalRefresh()


if __name__ == '__main__':
    # setup
    whoGoesFirst = randint(0, 1)
    gameOver = False

    boardSize = getBoardSize()
    logicBoard = initBoard(boardSize)

    print("Game Formatting Selection:")
    formatting = getDisplayFormat()

    print("Game Mode Selection:")
    mode = getGameMode()

    # Gameplay loops
    # TODO: make game wait for a click to happen
    if formatting == 1:
        terminalRefresh()
        turtle.screensize(600, 450)
        drawBoard(turtle, boardSize, turtle.screensize())

        # Computer game loop, turtle
        if mode == 1:
            print(f"Playing against the computer.\nPlayer {whoGoesFirst + 1} goes first!")
            computerGraphicalGame(gameOver, whoGoesFirst)

        # PvP game loop, turtle
        elif mode == 2:
            print(f"Playing against someone locally.\nPlayer {whoGoesFirst + 1} goes first!")
            pvpGraphicalGame(gameOver, whoGoesFirst)

    elif formatting == 2:
        terminalRefresh()
        # Computer game loop, terminal
        if mode == 1:
            print(f"Playing against the computer.\nPlayer {whoGoesFirst + 1} goes first!")
            computerTerminalGame(gameOver, whoGoesFirst)

        # PvP game loop, terminal
        elif mode == 2:
            print(f"Playing against someone locally.\nPlayer {whoGoesFirst + 1} goes first!")
            pvpTerminalGame(gameOver, whoGoesFirst)

    # TODO: make quitting actually shut everything down
    if formatting == 1:
        turtle.done()
