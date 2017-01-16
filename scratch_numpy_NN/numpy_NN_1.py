""" Notes:
define loss functions in Creature_Brain() (line 29)
"""
import numpy as np
import warnings
import os
from collections import defaultdict
# Local imports
import brains
import creatures


def clear_screen():
    pass

class Board(object):
    def __init__(self, n_tiles=100, tiles=None, features=2,
        tile_impact=5):
        """
        :param size: number of tiles
        :param tile_impact: int or float, highest absolute value of attribute
        :param features: number of features per tile
        :param tile_impact: multiplys the ablsolute values of features
        """
        self.impact = tile_impact
        self.tiles = tiles
        self.n_tiles = n_tiles
        self.features = features

    def randomize(self):
        self.tiles = (np.random.random_sample((self.n_tiles, self.features))
            * self.impact)


def main():
    ####################
    # Hyper Parameters #
    ####################
    name = input('What is your name? ')
    d_health = int(input('How much health do you have? '))
    n_tiles = int(input('How many tiles would you like in the board? '))
    n_runs = int(input(
        'And how many runs on this board would you like to do? '))

    ####################

    board = Board(n_tiles)
    test_guy = Creature(name, default_health=d_health)
    board.randomize()
    for run in range(n_runs):
        test_guy.reset(run)
        
        test_guy.board = board
        test_guy.run()



if __name__ == '__main__':
    bob = Creature('bobby', iNeurons=2, oNeurons=2)

    bob.print_network()
    

    input('game completed, press <enter> to exit')