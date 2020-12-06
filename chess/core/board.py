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

        self.initial_board = np.zeros([self.height, self.width], dtype=np.byte)
        self.__create_board_from_fen()
        self.current_board = np.copy(self.initial_board)

        self.board_size = self.__board_size()
        self.action_size = self.__action_size()
        self.square_index = self.height * self.width - 1
        
    def valid_moves(self, board):
        """ Returns all the valid movements for the current board. """
        self.current_board = board
        valid_moves = np.zeros(self.action_size, dtype=np.byte)

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
                self.initial_board[row][column] = Piece.get_number(piece_type)
                column += 1

    def __board_size(self):
        """ Returns the board size. """
        return (self.height, self.width)

    def __action_size(self):
        """ Returns the action size of the board. """
        total_positions = self.height ** 2 * self.width ** 2
        number_pieces = self.height * self.width
        return total_positions - number_pieces

    def __valid_moves_square(self, row, column, valid_moves):
        """ Returns all the possible moves from a specific position. """
        # Only the player can move him pieces
        if self.current_board[row][column] < 1:
            return
        
        movements = Piece.get_movement(self.current_board[row][column])

        for key, value in movements.items():
            if key == 'north':
                self.__valid_moves_north(row, column, valid_moves, value)
            elif key == 'south':
                self.__valid_moves_south(row, column, valid_moves, value)
            elif key == 'west':
                self.__valid_moves_west(row, column, valid_moves, value)
            elif key == 'east':
                self.__valid_moves_east(row, column, valid_moves, value)

    def __valid_moves_north(self, row, column, valid_moves, movement):
        """ Return all the possible moves going north from a specific position. """
        position = (row, column)
        position_index = np.ravel_multi_index(position, self.board_size)

        column_row = self.current_board[:, column][::-1] # Column of the row position
        start_row = self.height - row # The row where we begin to move
        max_row = self.height - 1 # As the column is reversed, we use this to obtain the not reversed row
        movement_range = start_row + movement # Range of the movement
        
        if movement_range > self.height:
            movement_range = self.height

        for i in range(start_row, movement_range):
            piece = column_row[i]

            if piece <= 0:
                new_position = (max_row - i, column)
                self.__register_valid_move(position_index, new_position, valid_moves)
            
            # The piece cannot jump
            if piece < 0 or piece > 0:
                break

    def __valid_moves_south(self, row, column, valid_moves, movement):
        """ Return all the possible moves going north from a specific position. """
        position = (row, column)
        position_index = np.ravel_multi_index(position, self.board_size)

        column_row = self.current_board[:, column] # Column of the row position
        start_row = row + 1 # The row where we begin to move
        movement_range = start_row + movement # Range of the movement
        
        if movement_range > self.height:
            movement_range = self.height

        for i in range(start_row, movement_range):
            piece = column_row[i]

            if piece <= 0:
                new_position = (i, column)
                self.__register_valid_move(position_index, new_position, valid_moves)
            
            # The piece cannot jump
            if piece < 0 or piece > 0:
                break

    def __valid_moves_west(self, row, column, valid_moves, movement):
        """ Return all the possible moves going west from a specific position. """
        position = (row, column)
        position_index = np.ravel_multi_index(position, self.board_size)

        row_column = self.current_board[row, :][::-1] # Row of the column position
        start_column = self.width - column # The column where we begin to move
        max_column = self.width - 1 # As the row is reversed, we use this to obtain the not reversed row
        movement_range = start_column + movement # Range of the movement
        
        if movement_range > self.width:
            movement_range = self.width

        for i in range(start_column, movement_range):
            piece = row_column[i]

            if piece <= 0:
                new_position = (row, max_column - i)
                self.__register_valid_move(position_index, new_position, valid_moves)
            
            # The piece cannot jump
            if piece < 0 or piece > 0:
                break

    def __valid_moves_east(self, row, column, valid_moves, movement):
        """ Return all the possible moves going east from a specific position. """
        position = (row, column)
        position_index = np.ravel_multi_index(position, self.board_size)

        row_column = self.current_board[row, :] # Row of the column position
        start_column = column + 1 # The column where we begin to move
        movement_range = start_column + movement # Range of the movement
        
        if movement_range > self.width:
            movement_range = self.width

        for i in range(start_column, movement_range):
            piece = row_column[i]

            if piece <= 0:
                new_position = (row, i)
                self.__register_valid_move(position_index, new_position, valid_moves)
            
            # The piece cannot jump
            if piece < 0 or piece > 0:
                break
    
    def __register_valid_move(self, position_index, new_position, valid_moves):
        """ Register a valid move. """
        new_position_index = np.ravel_multi_index(new_position, self.board_size)
        final_index = position_index * self.square_index + new_position_index
        valid_moves[final_index] = 1 # This is a valid move
