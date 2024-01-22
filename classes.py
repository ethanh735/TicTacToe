from random import randint

import main


class Piece:
    type: str

    def __init__(self, t: str):
        self.type = t

    def val(self):
        return self.type

    def place(self, board, x, y):
        board[x - 1][y - 1] = self.type

    @staticmethod
    def at(board, x, y):
        return board[x - 1][y - 1]


class GameObject:
    gameOver: bool
    whoGoesFirst: int
    boardSize: int
    logicBoard: [[]]
    formatting: int
    mode: int

    def __init__(self):
        self.gameOver = False
        self.whoGoesFirst = randint(0, 1)
        self.boardSize = main.getBoardSize()
        self.logicBoard = main.initBoard(self.boardSize)

        print("Game Formatting Selection:")
        self.formatting = main.getDisplayFormat()

        print("Game Mode Selection:")
        self.mode = main.getGameMode()