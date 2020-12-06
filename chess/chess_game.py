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
        return self.board.initial_board

    def getBoardSize(self):
        return self.board.board_size

    def getActionSize(self):
        return self.board.action_size

    def getNextState(self, board, player, action):
        self.board.move(board, action)
        return self.board.current_board, -player

    def getValidMoves(self, board, player):
        return self.board.valid_moves(board)

    def getGameEnded(self, board, player):
        pass

    def getCanonicalForm(self, board, player):
        # Swap player 1 to player -1
        return board * player

    def getSymmetries(self, board, pi):
        pass

    def stringRepresentation(self, board):
        return board.tostring()
