"""This class implements longest word game"""
# pylint: disable=too-few-public-methods
import random
import string
import requests
import json

class Game:
    """Class that implements Longest word game"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        return self.__in_grid(self.grid, word) and self.__in_dictionary(word)


    @staticmethod
    def __in_grid(grid: list, word: str) -> bool:
        return all(letter in grid for letter in word)

    @staticmethod
    def __in_dictionary(word: str) -> bool:
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}").json()
        return response['found']
