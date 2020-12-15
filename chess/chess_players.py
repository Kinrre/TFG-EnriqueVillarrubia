import numpy as np


class HumanChessPlayer():
    """
    A human chess player.
    """

    def __init__(self, game):
        self.game = game

    def play(self, board):
        valid_moves = self.game.getValidMoves(board, 1)
        board_size = self.game.getBoardSize()
        square_index = self.game.board.square_index

        print('\nMoves:', [(np.unravel_index(i // square_index, board_size), np.unravel_index(i % square_index, board_size), i) for (i, valid) in enumerate(valid_moves) if valid])

        while True:
            try:
                move = int(input())
            except ValueError:
                print("That's not a number")

            if valid_moves[move]:
                break
            else: 
                print('Invalid move')

        return move
