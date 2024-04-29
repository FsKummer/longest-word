from longest_word.game import *
import string
import random

class TestGame:
    def test_game_initialization(self):
           game = Game()
           grid = game.grid
           assert game != None
           assert type(grid) == list
           assert len(grid) == 9
           for letter in grid:
              assert letter in string.ascii_uppercase

    def test_is_valid(self):
        game = Game()
        grid = 'ABCDEFGHN'
        word = 'BANANA'
        game.grid = list(grid)
        assert game.is_valid(word) == True

    def test_is_valid_wrong_input(self):
        game = Game()
        word = '123'
        assert game.is_valid(word) == False

    def test_is_not_valid(self):
        game = Game()
        grid = 'ABCDEFGHI'
        word = 'NOTGOOD'
        game.grid = list(grid)
        assert game.is_valid(word) == False

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
