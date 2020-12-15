import numpy as np

from Arena import Arena
from MCTS import MCTS
from chess.chess_game import ChessGame
from chess.chess_players import HumanChessPlayer
from chess.keras.NNet import NNetWrapper
from utils import dotdict

g = ChessGame()
hp = HumanChessPlayer(g).play

n1 = NNetWrapper(g)
n1.load_checkpoint('./temp', 'best.pth.tar')

args1 = dotdict({'numMCTSSims': 100, 'cpuct': 1})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

arena = Arena(n1p, hp, g, display=ChessGame.display)

print(arena.playGames(2, verbose=True))
