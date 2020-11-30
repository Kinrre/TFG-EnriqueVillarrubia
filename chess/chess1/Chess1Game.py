import sys
import numpy as np

sys.path.append('..')
from Game import Game
from .Chess1Logic import Board


class Chess1Game(Game):
    """
    Chess1 Game class implementing the alpha-zero-general Game interface.
    """

    def __init__(self, height=None, width=None, fen=None):
        self.board = Board(height, width, fen)

    def getInitBoard(self):
        pass
