import numpy as np

from Arena import Arena
from MCTS import MCTS
from chess.chess_game import ChessGame
from chess.chess_players import HumanChessPlayer
from chess.keras.NNet import NNetWrapper
from utils import dotdict

g = ChessGame('examples/first_game.json')
hp = HumanChessPlayer(g).play

n1 = NNetWrapper(g)
n1.load_checkpoint('D:/modelos/chess/modelo1', 'checkpoint_1.pth.tar')

args1 = dotdict({'numMCTSSims': 30, 'cpuct': 1})
mcts1 = MCTS(g, n1, args1)
n1p = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

n2 = NNetWrapper(g)
n2.load_checkpoint('D:/modelos/chess/modelo1', 'best.pth.tar')

args2 = dotdict({'numMCTSSims': 30, 'cpuct': 1})
mcts2 = MCTS(g, n2, args2)
n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

arena = Arena(n1p, n2p, g, display=ChessGame.display)

print(arena.playGames(20, verbose=False))
