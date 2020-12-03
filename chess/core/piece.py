from utils import WHITE, BLACK, PIECES, R_PIECES, MOVEMENTS

class Piece:

    def __init__(self, piece_type=None, color=None):
        self.piece_type = piece_type
        self.color = color
        self.fen = '-'

        if self.piece_type != None and self.color != None:
            self.fen = R_PIECES[piece_type] # KeyError
            
            if color is WHITE:
                self.fen = self.fen.upper()

    @classmethod
    def from_fen(cls, fen):
        """ Create a piece from a fen piece. """
        piece_type = PIECES[fen.lower()] # KeyError
        color = WHITE if fen.isupper() else BLACK

        return cls(piece_type, color)

    @staticmethod
    def get_number(fen):
        """ Return the number corresponding to a piece. """
        return PIECES[fen] # KeyError
    
    @staticmethod
    def get_movement(number):
        """ Return the movement corresponding to a piece. """
        return MOVEMENTS[number] # KeyError

    def __repr__(self):
        return self.fen
