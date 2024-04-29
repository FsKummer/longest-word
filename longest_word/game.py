"""This class implements longest word game"""
# pylint: disable=too-few-public-methods
import random
import string

class Game:
    """Class that implements Longest word game"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        return all(letter in self.grid for letter in word)
