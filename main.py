import turtle
from random import randint
import classes


def initBoard(size):
    board = [[] for i in range(size)]
    for rows in range(size):
        for cols in range(size):
            board[rows].append(0)
    return board


def drawBoard(t, bSize, sSize):
    # setup
    scale = sSize[0] / bSize
    t.tracer(2, 0)
    t.pensize(15 / bSize)
    t.hideturtle()
    x = y = -scale * (bSize / 2)
    t.penup()
    t.setpos(x, y + scale)
    t.pendown()

    # Drawing of board
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

    x += scale
    for j in range(bSize - 1):
        t.setheading(90)
        t.forward(sSize[0])
        x += scale
        t.penup()
        t.setpos(x, y)
        t.pendown()


# TODO: handle strings that aren't num, num
def terminalPlace(player):
    # Emulates a do-while loop
    while True:
        x = y = -1
        i = input()

        # Input handling
        if i == "end" or i == "quit" or i == "stop":
            return True
        elif 3 <= i.__len__() <= 6:
            x, y = i.split(",")
            x = int(x)
            y = int(y)

        # Valid placement conditions
        if logicBoard[x - 1][y - 1] == 0 <= x <= boardSize and 0 <= y <= boardSize:
            break
        else:
            print("Invalid placement, enter another coordinate:")

    player.place(logicBoard, x, y)
    return False


def graphicalPlace(x, y, bSize, sSize):
    # Emulates a do-while loop
    while True:
        print("Which tile is the click in?")
        break
        # Figure out which spot the click coordinates are in
        # instance - 1 / boardSize:
        # Board of 4: between 1/6 and 2/6 screenSize, 2/6 and 3/6 screenSize, 3/6 and 4/6 screenSize, 4/6 and 5/6 screenSize


# TODO: distinguish between terminal and turtle modes
if __name__ == '__main__':

    # 1. turtle vs terminal
    # 2. another player vs computer
    # 3. gameplay loop: X vs O

    # setup
    # 1. turtle
    #   2. player
    #       3. loop
    #   2. computer
    #       3. loop
    # 1. terminal
    #   2. player
    #       3. loop
    #   2. computer
    #       3. loop

    # TODO: make game format a function
    # Board creation
    boardSize = 3
    logicBoard = initBoard(boardSize)

    # Selecting game representation
    print("Game Formatting Selection:")
    formatMode = int(input("Press 1 to play on a graphical screen, or 2 to play a text-based game: "))
    while formatMode < 1 or formatMode > 2:
        formatMode = int(input("Invalid game format, enter a valid option: "))

    if formatMode == 1:
        turtle.screensize(600, 450)
        drawBoard(turtle, boardSize, turtle.screensize())

    # TODO: make game mode a function
    # Selecting game mode
    print("Game Mode Selection:")
    gameMode = int(input("Press 1 to play against the computer, or 2 to play against another person locally: "))
    while gameMode != 2:
        gameMode = int(input("Invalid game mode, enter a valid option: "))
    first = randint(0, 1)

    # Gameplay loops
    gameOver = False
    plays = 0

    # PvP game loop, turtle
    if gameMode == 2 and formatMode == 1:
        print(f"Playing against someone locally.\nPlayer {first + 1} goes first!")
        while not gameOver:
            countForX = countForO = 0

            if first == 0:
                plays += 1
                print("X's turn! click any valid spot on the board.")
                turtle.onclick(graphicalPlace)

                first = not first

            elif first == 1:
                plays += 1
                print("O's turn! click any valid spot on the board.")
                turtle.onclick(turtle.goto)
                graphicalPlace(turtle.xcor(), turtle.ycor(), boardSize, turtle.screensize())

                first = not first


    # # Computer game loop, terminal
    # elif gameMode == 1 and formatMode == 2:
    #     print("Playing against the computer.")
    #     if first == 0:
    #         print("You go first!")
    #     else:
    #         print("The computer goes first!")
    #     while not gameOver:
    #         countForX = countForO = 0
    #         if first == 0:
    #             first = not first
    #
    #         elif first == 1:
    #             first = not first
    #
    #         # Terminal board representation
    #         for row in range(boardSize):
    #             print(logicBoard[row])
    #
    #         # Win condition
    #         if countForX == boardSize:
    #             gameOver = True
    #             print("Game Over! X wins!")
    #         elif countForO == boardSize:
    #             gameOver = True
    #             print("Game Over! O wins!")
    #         elif plays == boardSize * boardSize:
    #             gameOver = True
    #             print("It's a draw!")

    # PvP game loop, terminal
    elif gameMode == 2 and formatMode == 2:
        print(f"Playing against someone locally.\nPlayer {first + 1} goes first!")
        while not gameOver:
            countForX = countForO = 0

            if first == 0:
                plays += 1
                # first player X: wherever click is, place an X on the board
                print(f"X's turn! Enter coordinates between 1,1 and {boardSize},{boardSize}:")
                gameOver = terminalPlace(classes.X())

                # if piece in first row, check below
                for col in range(boardSize):
                    if isinstance(logicBoard[0][col], classes.X):
                        countForX = 1
                        for row in range(boardSize - 1):
                            if isinstance(logicBoard[row + 1][col], classes.X):
                                countForX += 1

                # if in first column of other rows, check right
                for row in range(boardSize):
                    if isinstance(logicBoard[row][0], classes.X):
                        countForX = 1
                        for col in range(boardSize - 1):
                            if isinstance(logicBoard[row][col + 1], classes.X):
                                countForX += 1

                first = not first

            elif first == 1:
                plays += 1
                # second player O: wherever click place O on board
                print(f"O's turn! Enter coordinates between 1,1 and {boardSize},{boardSize}:")
                gameOver = terminalPlace(classes.O())

                # if piece in first row, check below
                for col in range(boardSize):
                    if isinstance(logicBoard[0][col], classes.O):
                        countForO = 1
                        for row in range(boardSize - 1):
                            if isinstance(logicBoard[row + 1][col], classes.O):
                                countForO += 1

                # if in first column of other rows, check right
                for row in range(boardSize):
                    if isinstance(logicBoard[row][0], classes.O):
                        countForO = 1
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
