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

    # # decorator: sets value of global variable to assume a value for future tests
    # @patch('main.boardSize', 3)
    # def testGameplay(self):
    #     with patch("builtins.input", side_effect=["3", "2", "2", "3,3", "1,2", "2,3", "2,2", "1,3"]):
    #         self.assertEqual(main.pvpTerminalGame(False, 1))
    #         self.assertEqual(main.pvpTerminalGame(False, 2))


if __name__ == '__main__':
    unittest.main()
