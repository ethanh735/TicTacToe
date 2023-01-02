import turtle
from random import randint
import re

import classes


def initBoard(size):
    board = [[] for i in range(size)]
    for row in range(size):
        for col in range(size):
            board[row].append(0)
    return board


# TODO: regulate board size scale to current screen size
def drawBoard(t, board):
    # setup
    scale = -20 * board.__len__() + 300
    t.tracer(0)
    t.pensize(4)
    t.color("black")
    x = y = -scale * (board.__len__() / 2)
    t.penup()
    t.setpos(x, y)
    t.pendown()

    # does this really need to be N^3
    for row in board:
        for tile in row:
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
    i = input()
    if i == "end" or i == "quit" or i == "stop":
        return True
    x, y = i.split(",")
    x = int(x)
    y = int(y)

    # Conditions for valid placement: if invalid, must enter input again
    while not (boardSize >= x >= 0 == logicBoard[x - 1][y - 1] and boardSize >= y >= 0):
        print("Invalid placement, enter another coordinate:")
        i = input()
        if i == "end" or i == "quit" or i == "stop":
            return True
        x, y = i.split(",")
        x = int(x)
        y = int(y)

    # player.place(logicBoard, x, y)
    logicBoard[x - 1][y - 1] = player
    print(logicBoard)
    return False


if __name__ == '__main__':

    # Board creation
    boardSize = 3
    logicBoard = initBoard(boardSize)
    drawBoard(turtle, logicBoard)

    # Selecting game mode
    gameMode = int(input("Press 1 to play against the computer, or 2 to play against another person locally: "))
    first = randint(0, 1)
    while gameMode < 1 or gameMode > 2:
        gameMode = int(input("Invalid game mode, enter a valid option: "))

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

    # TODO: win condition
    while not gameOver:
        if first == 0:
            # first player X: wherever click is, place an X on the board
            print(f"X's turn! Enter coordinates between 1,1 and {boardSize},{boardSize}:")
            gameOver = terminalPlace(classes.X())

            # if piece in first row, check below: if in first column of other rows, check right
            for row in range(boardSize):
                for col in range(boardSize):
                    print(row, col, type(logicBoard[row][col]), type(classes.X()))
                    # First row: check if other pieces are below
                    if logicBoard[row][col] == classes.X() and row == 0:
                        print("Top", end='')
                    # First col: check if pieces are right
                    elif logicBoard[row][col] == classes.X() and col == 0:
                        print("Left", end='')

            first = not first

        else:
            # second player O: wherever click place O on board
            print(f"O's turn! Enter coordinates between 1,1 and {boardSize},{boardSize}:")
            gameOver = terminalPlace(classes.O())

            # if piece in first row, check below: if in first column of other rows, check right
            for row in range(boardSize):
                for col in range(boardSize):
                    print(row, col, type(logicBoard[row][col]), type(classes.O()))
                    # First row: check if other pieces are below
                    if logicBoard[row][col] == classes.O() and row == 0:
                        print("Top", end='')
                    # First col: check if pieces are right
                    elif logicBoard[row][col] == classes.O() and col == 0:
                        print("Left", end='')

            first = not first

    # TODO: make quitting actually shut everything down
    print("Game over!")
    turtle.done()
