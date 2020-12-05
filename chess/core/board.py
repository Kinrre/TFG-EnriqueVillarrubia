import numpy as np
from piece import Piece

DEFAULT_HEIGHT = 6
DEFAULT_WIDTH = 6
DEFAULT_BOARD = '1rqkr1/1pppp1/6/6/1PPPP1/1RQKR1'


class Board():
    """
    Chess board.
    """

    def __init__(self, height=None, width=None, fen=None):
        """ Set up initial board configuration. """
        # TODO: Only with the fen string is necessary
        self.height = height or DEFAULT_HEIGHT
        self.width = width or DEFAULT_WIDTH
        self.fen = fen or DEFAULT_BOARD

        self.board = np.zeros([self.height, self.width], dtype=np.byte)
        self.__create_board_from_fen()
        
    def valid_moves(self):
        """ Returns all the valid movements for the board. """
        valid_moves = []

        for row in range(self.height):
            for column in range(self.width):
                self.__valid_moves_square(row, column, valid_moves)

        return valid_moves

    def __create_board_from_fen(self):
        """ Create the board from a string in fen notation. """
        row = 0
        column = 0

        for piece_type in self.fen:
            if piece_type.isdigit():
                column += int(piece_type)
            elif piece_type == '/':
                row += 1
                column = 0
            else:
                self.board[row][column] = Piece.get_number(piece_type)
                column += 1

    def __valid_moves_square(self, row, column, valid_moves):
        """ Returns all the possible moves from a specific position. """
        # Only the player can move him pieces
        if self.board[row][column] < 1:
            return []
        
        movements = Piece.get_movement(self.board[row][column])

        for key, value in movements.items():
            if key == 'north':
                self.__valid_moves_north(row, column, valid_moves, value)
            elif key == 'south':
                self.__valid_moves_south(row, column, valid_moves, value)
            elif key == 'west':
                self.__valid_moves_west(row, column, valid_moves, value)

    def __valid_moves_north(self, row, column, valid_moves, movement):
        """ Return all the possible moves going north from a specific position. """
        position = (row, column)

        column_row = self.board[:, column][::-1] # Column of the row position
        start_row = self.height - row # The row where we begin to move
        original_row = self.height - 1 # As the column is reversed, this is the original_row
        movement_range = start_row + movement # Range of the movement
        
        if movement_range > self.height:
            movement_range = self.height

        for i in range(start_row, movement_range):
            piece = column_row[i]

            if piece <= 0:
                new_position = (original_row - i, column)
                valid_moves.append([position, new_position])
            
            # The piece cannot jump
            if piece < 0 or piece > 0:
                break

    def __valid_moves_south(self, row, column, valid_moves, movement):
        """ Return all the possible moves going north from a specific position. """
        position = (row, column)

        column_row = self.board[:, column] # Column of the row position
        start_row = row + 1 # The row where we begin to move
        movement_range = start_row + movement # Range of the movement
        
        if movement_range > self.height:
            movement_range = self.height

        for i in range(start_row, movement_range):
            piece = column_row[i]

            if piece <= 0:
                new_position = (i, column)
                valid_moves.append([position, new_position])
            
            # The piece cannot jump
            if piece < 0 or piece > 0:
                break

    def __valid_moves_west(self, row, column, valid_moves, movement):
        """ Return all the possible moves going west from a specific position. """
        position = (row, column)

        row_column = self.board[row, :][::-1] # Row of the column position
        start_column = self.width - column # The column where we begin to move
        original_column = self.width - 1 # As the row is reversed, this is the original_column
        movement_range = start_column + movement # Range of the movement
        
        if movement_range > self.width:
            movement_range = self.width

        for i in range(start_column, movement_range):
            piece = row_column[i]

            if piece <= 0:
                new_position = (row, original_column - i)
                valid_moves.append([position, new_position])
            
            # The piece cannot jump
            if piece < 0 or piece > 0:
                break
