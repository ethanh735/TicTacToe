class X:

    def __init__(self):
        self

    def place(self, board, x, y):
        board[x - 1][y - 1] = X()


class O:

    def __init__(self):
        self

    def place(self, board, x, y):
        board[x - 1][y - 1] = O()
