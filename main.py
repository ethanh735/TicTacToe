import turtle
from os import system, name

import classes


def initBoard(size):
    # List of lists
    board = [[] for _ in range(size)]
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
                x = int(x)
                y = int(y)
            except ValueError or AssertionError:
                print(f"Invalid format, enter a valid coordinate as num,num:")
                continue
            # Valid placement conditions
            else:
                if 0 < x <= game.boardSize and 0 < y <= game.boardSize and game.logicBoard[x - 1][y - 1] == '-':
                    break
                print(f"Invalid placement, enter another coordinate between 1,1 and {game.boardSize},{game.boardSize}:")

    player.place(game.logicBoard, x, y)
    return False


def terminalRefresh():
    # terminal clearing based on OS type
    if name == 'nt':
        system('cls')
    elif name == 'posix':
        system('clear')
    # proper formatting for each row
    for row in range(game.boardSize):
        print(game.logicBoard[row])


# def graphicalPlace(x, y, bSize, sSize):
#     return
#     # while True:
#     #     print("Which tile is the click in?")
#     #     break
#     #     # Figure out which spot the click coordinates are in
#     #     # instance - 1 / game.boardSize:
#     #     # Board of 4: between 1/6 and 2/6 screenSize, 2/6 and 3/6 screenSize, 3/6 and 4/6 screenSize, 4/6 and 5/6 screenSize (if centered by equidistant margins)


# def computerGraphicalGame(over, first):
#     return

# TODO: implement graphical placement
# TODO: implement graphical win condition
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
                # graphicalPlace(turtle.xcor(), turtle.ycor(), game.boardSize, turtle.screensize())
                print(turtle.pos())

            first = not first
            over = True

        elif first == 1:
            plays += 1
            print("O's turn! click any valid spot on the board.")
            # Wait for a click to happen
            while turtx == turtle.xcor() and turty == turtle.ycor():
                turtle.onclick(turtle.goto)
                # graphicalPlace(turtle.xcor(), turtle.ycor(), game.boardSize, turtle.screensize())
                print(turtle.pos())

            first = not first
            over = True


# def computerTerminalGame(over, first):
#     return
#     # plays = 0
#     #
#     # if first == 0:
#     #     print("You go first!")
#     # else:
#     #     print("The computer goes first!")
#     # while not over:
#     #     countX = countO = 0
#     #     if first == 0:
#     #         first = not first
#     #
#     #     elif first == 1:
#     #         first = not first
#
#     #     # Terminal board representation
#     #     for row in range(game.boardSize):
#     #         print(game.logicBoard[row])
#     #
#     #     over = terminalWin(countX, countO, plays)


def pvpTerminalGame(over, first):
    plays = 0
    while not over:
        count = 1

        # Tie Game
        if plays == game.boardSize ** 2:
            print("It's a draw!")
            over = True

        # X plays
        piece = classes.Piece('X')
        # O plays
        if first == 1:
            piece = classes.Piece('O')

        plays += 1

        # per turn, wherever coordinates are, place a piece on the board
        print(f"{piece.val()}'s turn! Enter coordinates between 1,1 and {game.boardSize},{game.boardSize}:")
        if terminalPlace(piece):
            break

        # Win Condition Checking:
        # \ diagonal check: if top left corner is piece.val() then check
        if game.logicBoard[0][0] == piece.val():
            for row_col in range(1, game.boardSize):
                if game.logicBoard[row_col][row_col] == piece.val():
                    count += 1
        # determine if win has occurred
        if count >= game.boardSize:
            over = True
        else:
            count = 1

        # / diagonal check: if top right corner is piece.val() then check
        if game.logicBoard[0][game.boardSize - 1] == piece.val():
            col = game.boardSize - 2
            for row in range(1, game.boardSize):
                if game.logicBoard[row][col] == piece.val():
                    count += 1
                col -= 1
        # determine if win has occurred
        if count >= game.boardSize:
            over = True
        else:
            count = 1

        for start in range(game.boardSize):
            # - vertical check: if top row is piece.val() then check
            if game.logicBoard[0][start] == piece.val():
                for row in range(1, game.boardSize):
                    if game.logicBoard[row][start] == piece.val():
                        count += 1
            # determine if win has occurred
            if count >= game.boardSize:
                over = True
            else:
                count = 1

            # | horizontal check: if start column is piece.val() then check
            if game.logicBoard[start][0] == piece.val():
                for col in range(1, game.boardSize):
                    if game.logicBoard[start][col] == piece.val():
                        count += 1
            # determine if win has occurred
            if count >= game.boardSize:
                over = True
            else:
                count = 1

        # prep for next turn
        first = not first
        terminalRefresh()
        if over:
            print(f"Game Over! {piece.val()} wins!")


if __name__ == '__main__':
    # setup
    game = classes.GameObject()

    # Gameplay loops
    # TODO: make game wait for a click to happen
    if game.formatting == 1:
        terminalRefresh()
        turtle.screensize(600, 450)
        drawBoard(turtle, game.boardSize, turtle.screensize())

        # Computer game loop, turtle
        if game.mode == 1:
            print(f"Playing against the computer.\nPlayer {game.whoGoesFirst + 1} goes first!")
            # computerGraphicalGame(game.gameOver, game.whoGoesFirst)

        # PvP game loop, turtle
        elif game.mode == 2:
            print(f"Playing against someone locally.\nPlayer {game.whoGoesFirst + 1} goes first!")
            pvpGraphicalGame(game.gameOver, game.whoGoesFirst)

    elif game.formatting == 2:
        terminalRefresh()
        # Computer game loop, terminal
        if game.mode == 1:
            print(f"Playing against the computer.\nPlayer {game.whoGoesFirst + 1} goes first!")
            # computerTerminalGame(game.gameOver, game.whoGoesFirst)

        # PvP game loop, terminal
        elif game.mode == 2:
            print(f"Playing against someone locally.\nPlayer {game.whoGoesFirst + 1} goes first!")
            pvpTerminalGame(game.gameOver, game.whoGoesFirst)

    # TODO: make quitting actually shut everything down
    if game.formatting == 1:
        turtle.done()
