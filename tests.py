import unittest
from unittest import mock

import main


class MyTestCase(unittest.TestCase):

    def testUserInput(self):
        # built-in input function is given list of inputs, run through in order by respective tests
        # getBoardSize:
        with mock.patch("builtins.input", side_effect=["102", "4", "-6", "38", -2, 5, "word", "3"]):
            self.assertEqual(main.getBoardSize(), 4)
            self.assertEqual(main.getBoardSize(), 38)
            self.assertEqual(main.getBoardSize(), 5)
            self.assertEqual(main.getBoardSize(), 3)

        # getDisplayFormat:
        with mock.patch("builtins.input", side_effect=["-1", "word", "1", "4", 1, "2"]):
            self.assertEqual(main.getDisplayFormat(), 1)
            self.assertEqual(main.getDisplayFormat(), 2)
            
        # getGameMode:
        with mock.patch("builtins.input", side_effect=["-1", "word", "1", "4", 1, "2"]):
            # self.assertEqual(main.getGameMode(), 1)
            self.assertEqual(main.getGameMode(), 2)


if __name__ == '__main__':
    unittest.main()
