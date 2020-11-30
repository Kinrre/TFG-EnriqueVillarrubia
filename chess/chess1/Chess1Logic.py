import numpy as np
import core

DEFAULT_HEIGHT = 6
DEFAULT_WIDTH = 6
DEFAULT_BOARD = '1rqkr1/1pppp1/6/6/1PPPP1/1RQKR1'

class Board():
    """
    Chess1 Board.
    """

    def __init__(self, height=None, width=None, fen=None):
        "Set up initial board configuration."
        self.height = height or DEFAULT_HEIGHT
        self.width = width or DEFAULT_WIDTH
        self.fen = fen or DEFAULT_BOARD

        self.board = np.zeros([self.height, self.width], dtype=core.Piece)
        self._create_board_from_fen(DEFAULT_BOARD)
        
    def _create_board_from_fen(self, fen):
        row = 0
        column = 0

        for piece_type in fen:
            if piece_type.isdigit():
                for i in range(0, int(piece_type)):
                    self.board[row][column] = core.Piece()
                    column += 1
            elif piece_type == '/':
                row += 1
                column = 0
            else:
                self.board[row][column] = core.Piece.from_fen(piece_type)
                column += 1
