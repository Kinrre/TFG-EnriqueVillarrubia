import board
fen = '1pppp1/6/P5/1PPPP1'

b = board.Board(4, 6, fen)
#b.board *= -1
valid_moves = b.valid_moves(b.current_board)

print(b.initial_board)
print(valid_moves)
print(len(valid_moves))

for i in range(len(valid_moves)):
    if valid_moves[i] == 1:
        b.move(b.initial_board, i)
        print(i)
        print(b.current_board)
