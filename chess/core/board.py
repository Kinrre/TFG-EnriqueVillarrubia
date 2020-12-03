import numpy as np
from piece import PIECES 

DEFAULT_HEIGHT = 6
DEFAULT_WIDTH = 6
DEFAULT_BOARD = '1rqkr1/1pppp1/6/6/1PPPP1/1RQKR1'


class Board():
    """
    Chess board.
    """

    def __init__(self, height=None, width=None, fen=None):
        """Set up initial board configuration."""
        self.height = height or DEFAULT_HEIGHT
        self.width = width or DEFAULT_WIDTH
        self.fen = fen or DEFAULT_BOARD

        self.board = np.zeros([self.height, self.width], dtype=np.byte)
        self._create_board_from_fen()
        
    def _create_board_from_fen(self):
        """Create the board from a string in fen notation."""
        row = 0
        column = 0

        for piece_type in self.fen:
            if piece_type.isdigit():
                column += int(piece_type)
            elif piece_type == '/':
                row += 1
                column = 0
            else:
                self.board[row][column] = PIECES[piece_type] # IndexError
                column += 1

    def valid_moves_square(self, x, y):
        # Only the player can move him pieces
        if self.board[x][y] < 1:
            return []
        
        valid_moves = []
        
        # North movement (2, 1)
        self.valid_moves_north(x, y, valid_moves)
            
        return valid_moves

    def valid_moves_north(self, x, y, valid_moves):
        position = (x, y)

        column = self.board[:, y][::-1]
        start_x = self.height - x
        # As we are indexing in reverse order, we need to return the original row
        original_row = self.height - 1

        for i in range(start_x, self.height):
            piece = column[i]

            if piece <= 0:
                new_position = (original_row - i, y)
                valid_moves.append((position, new_position))
            
            if piece < 0 or piece > 0:
                break
