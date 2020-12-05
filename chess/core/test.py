import board
fen = '1pppp1/6/P5/1PPPP1'

b = board.Board(4, 6, fen)
#b.board *= -1
print(b.initial_board)
print(b.valid_moves())
print(len(b.valid_moves()))
