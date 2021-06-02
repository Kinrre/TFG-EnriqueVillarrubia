import argparse
import coloredlogs
import logging

from Coach import Coach
from chess.chess_game import ChessGame as Game
from chess.keras.NNet import NNetWrapper as nn
from utils import *

log = logging.getLogger(__name__)

coloredlogs.install(level='INFO')  # Change this to DEBUG to see more info.

args = dotdict({
    'numIters': 100,
    'numEps': 15,              # Number of complete self-play games to simulate during a new iteration.
    'tempThreshold': 10,        #
    'updateThreshold': 0.6,     # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'maxlenOfQueue': 200000,    # Number of game examples to train the neural networks.
    'numMCTSSims': 30,          # Number of games moves for MCTS to simulate.
    'arenaCompare': 20,         # Number of games to play during arena play to determine if new net will be accepted.
    'cpuct': 1,

    'checkpoint': 'D:/modelos/chess/modelo2',
    'load_model': False,
    'load_folder_file': ('temp/', 'best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,
})


def main(game_configuration):
    log.info('Loading %s...', Game.__name__)
    g = Game(game_configuration)

    log.info('Loading %s...', nn.__name__)
    nnet = nn(g)

    if args.load_model:
        log.info('Loading checkpoint "%s/%s"...', args.load_folder_file[0], args.load_folder_file[1])
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])
    else:
        log.warning('Not loading a checkpoint!')

    log.info('Loading the Coach...')
    c = Coach(g, nnet, args)

    if args.load_model:
        log.info("Loading 'trainExamples' from file...")
        c.loadTrainExamples()

    log.info('Starting the learning process 🎉')
    c.learn()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Path to a JSON game configuration. See examples folder.')
    
    parser_args = parser.parse_args()

    with open(parser_args.path, 'r') as f:
        content = f.read()

    main(content)
