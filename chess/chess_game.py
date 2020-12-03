import sys

sys.path.append('..')
from Game import Game
from .Chess1Logic import Board


class ChessGame(Game):
    """
    ChessGame class implementing the alpha-zero-general Game interface.
    """

    def __init__(self, height=None, width=None, fen=None):
        self.board = Board(height, width, fen)

    def getInitBoard(self):
        return self.board

    def getBoardSize(self):
        return (self.board.height, self.board.width)

    def getActionSize(self):
        total_positions = self.board.height ** 2 * self.board.width ** 2
        number_pieces = self.board.height * self.board.width
        return total_positions - number_pieces

    def getNextState(self, board, player, action):
        pass

    def getValidMoves(self, board, player):
        pass

    def getGameEnded(self, board, player):
        pass

    def getCanonicalForm(self, board, player):
        # Swap player 1 to player -1
        return board * player

    def getSymmetries(self, board, pi):
        pass

    def stringRepresentation(self, board):
        return board.tostring()
