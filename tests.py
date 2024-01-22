import unittest
from unittest.mock import patch

import main


class MyTestCase(unittest.TestCase):

    def testUserInput(self):
        # built-in input function is given list of inputs, run through in order by respective tests
        # getBoardSize:
        with patch("builtins.input", side_effect=["102", "4", "-6", "38", -2, 5, "word", "3"]):
            self.assertEqual(main.getBoardSize(), 4)
            self.assertEqual(main.getBoardSize(), 38)
            self.assertEqual(main.getBoardSize(), 5)
            self.assertEqual(main.getBoardSize(), 3)

        # getDisplayFormat:
        with patch("builtins.input", side_effect=["-1", "word", "1", "4", 1, "2"]):
            self.assertEqual(main.getDisplayFormat(), 1)
            self.assertEqual(main.getDisplayFormat(), 2)

        # getGameMode:
        with patch("builtins.input", side_effect=["-1", "word", "1", "4", 1, "2"]):
            # self.assertEqual(main.getGameMode(), 1)
            self.assertEqual(main.getGameMode(), 2)

    @staticmethod
    def resetGame(obj, first, size, form, mode):
        # initialize all game variables
        obj.gameOver = False
        obj.whoGoesFirst = first
        obj.boardSize = size
        obj.logicBoard = main.initBoard(obj.boardSize)
        # obj.formatting = form
        # obj.mode = mode
        main.game = obj

    # decorator: sets value of global variable to assume a value for future tests
    @patch('classes.GameObject')
    def testGameplayVertical(self, mockGameObject):
        # Vertical X
        self.resetGame(mockGameObject, 0, 3, 2, 2)
        with patch("builtins.input", side_effect=["3,3", "1,2", "3", "2,3", "2,2", "4,2", "1,3"]):
            self.assertEqual(main.pvpTerminalGame(mockGameObject.gameOver, mockGameObject.whoGoesFirst), None)
        # Vertical O
        self.resetGame(mockGameObject, 1, 3, 2, 2)
        with patch("builtins.input", side_effect=["3,3", "1,2", "3", "2,3", "2,2", "4,2", "1,3"]):
            self.assertEqual(main.pvpTerminalGame(mockGameObject.gameOver, mockGameObject.whoGoesFirst), None)
        # Vertical Big Board
        self.resetGame(mockGameObject, 0, 4, 2, 2)
        with patch("builtins.input", side_effect=["2,3", "3,4", "4,5", "1,3", "4,1", "22", "4,3", "2,2", "2,3", "3,3"]):
            self.assertEqual(main.pvpTerminalGame(mockGameObject.gameOver, mockGameObject.whoGoesFirst), None)

    @patch('classes.GameObject')
    def testGameplayHorizontal(self, mockGameObject):
        # Horizontal X
        self.resetGame(mockGameObject, 0, 3, 2, 2)
        with patch("builtins.input", side_effect=["2,1", "3,2", "4,4", "2,2", "3,1", "2,1", "2,3"]):
            self.assertEqual(main.pvpTerminalGame(mockGameObject.gameOver, mockGameObject.whoGoesFirst), None)
        # Horizontal O
        self.resetGame(mockGameObject, 1, 3, 2, 2)
        with patch("builtins.input", side_effect=["2,1", "3,2", "4,4", "2,2", "3,1", "2,1", "2,3"]):
            self.assertEqual(main.pvpTerminalGame(mockGameObject.gameOver, mockGameObject.whoGoesFirst), None)
        # Horizontal Big Board
        self.resetGame(mockGameObject, 0, 4, 2, 2)
        with patch("builtins.input", side_effect=["4,1", "3,3", "4", "2,1", "3,1", "3,3", "1,3", "3,4", "0,2", "1,1", "3,2"]):
            self.assertEqual(main.pvpTerminalGame(mockGameObject.gameOver, mockGameObject.whoGoesFirst), None)

    @patch('classes.GameObject')
    def testGameplayDiagonal(self, mockGameObject):
        # Front Diagonal
        self.resetGame(mockGameObject, 0, 3, 2, 2)
        with patch("builtins.input", side_effect=["2,2", "3,1", "0,0", "3,3", "2,1", "0,1", "1,1"]):
            self.assertEqual(main.pvpTerminalGame(mockGameObject.gameOver, mockGameObject.whoGoesFirst), None)
        # Back Diagonal
        self.resetGame(mockGameObject, 1, 3, 2, 2)
        with patch("builtins.input", side_effect=["1,3", "1,2", "-1", "2,2", "3,3", "2,-1", "3,1"]):
            self.assertEqual(main.pvpTerminalGame(mockGameObject.gameOver, mockGameObject.whoGoesFirst), None)


if __name__ == '__main__':
    unittest.main()
