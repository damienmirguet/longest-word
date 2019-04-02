# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_is_valid_return_bool(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(new_game.is_valid("A",grid),bool)

    def test_null_string_is_not_valid(self):
        new_game = Game()
        self.assertIs(new_game.is_valid('',new_game.grid),False)

    def test_validword_is_valid(self):
        new_game = Game()
        new_game.grid = ['A','B','C','D']
        self.assertIs(new_game.is_valid('ABC',new_game.grid),True)

    def test_NOTvalidword_is_not_valid(self):
        new_game = Game()
        new_game.grid = ['A','B','C','D']
        self.assertIs(new_game.is_valid('XYZ',new_game.grid),False)
