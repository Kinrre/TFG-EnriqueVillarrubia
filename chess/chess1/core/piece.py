WHITE = 1
BLACK = 0

PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

PIECES = {'p': PAWN, 'k': KNIGHT, 'b': BISHOP, 'r': ROOK, 'q': QUEEN, 'k': KING}
R_PIECES = {PAWN: 'p', KNIGHT: 'k', BISHOP: 'b', ROOK: 'r', QUEEN: 'q', KING: 'k'}

class Piece:

    def __init__(self, piece_type=None, color=None):
        self.piece_type = piece_type
        self.color = color
        self.fen = '-'

        if self.piece_type != None and self.color != None:
            self.fen = R_PIECES[piece_type]
            
            if color is WHITE:
                self.fen = self.fen.upper()

    @classmethod
    def from_fen(cls, fen):
        """ Create a piece from a fen piece. """
        piece_type = PIECES[fen.lower()]
        color = WHITE if fen.isupper() else BLACK

        return Piece(piece_type, color)

    def __repr__(self):
        return self.fen
