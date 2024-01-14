def at(board, x, y):
    return board[x - 1][y - 1]


class PieceX:

    def __init__(self):
        self

    def val(self):
        return 'X'

    def place(self, board, x, y):
        board[x - 1][y - 1] = 'X'


class PieceO:

    def __init__(self):
        self

    def val(self):
        return 'O'

    def place(self, board, x, y):
        board[x - 1][y - 1] = 'O'
