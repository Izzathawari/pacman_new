import unittest
from unittest.mock import patch
from user_input import UserInput


class TestUserInput(unittest.TestCase):

    #unittest を使うとメソッドの機能を確認すること

    # unittest can verify the method functionality

    @patch("builtins.input", side_effect=["w"])
    def test_get_user_input_A_up(self, mock_input):
        expected = (0, -1)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result) #assertEqual(1番目の引数、2番目の引数) は1番目の引数と2番目の引数を比較すること

    @patch("builtins.input", side_effect=["a"])
    def test_get_user_input_B_left(self, mock_input):
        expected = (-1, 0)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=["s"])
    def test_get_user_input_C_down(self, mock_input):
        expected = (0, 1)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=["d"])
    def test_get_user_input_D_right(self, mock_input):
        expected = (1, 0)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=["x"])
    def test_get_user_input_E_invalid(self, mock_input):
        expected = (0, 0)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()