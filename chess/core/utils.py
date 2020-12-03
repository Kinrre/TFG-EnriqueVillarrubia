WHITE = 1
BLACK = 0

PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

PIECES = {'p': -PAWN, 'k': -KNIGHT, 'b': -BISHOP, 'r': -ROOK, 'q': -QUEEN, 'k': -KING,
          'P': PAWN, 'K': KNIGHT, 'B': BISHOP, 'R': ROOK, 'Q': QUEEN, 'K': KING}
R_PIECES = {PAWN: 'p', KNIGHT: 'k', BISHOP: 'b', ROOK: 'r', QUEEN: 'q', KING: 'k'}

MOVEMENTS = {PAWN: {'north': 1, 'south': 1, 'west': 1, 'east': 1}}
