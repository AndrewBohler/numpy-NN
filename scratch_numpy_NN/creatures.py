import numpy as np
import warnings
import os
import names
from collections import defaultdict
import brains

class Default(object):
    """
    Default Creature class, inherits form Creature_Brain
    """
    def __init__(self, name=names.get_full_name(), maxHealth=100,
        maxEnergy=100, **kwargs):
        self.brain = brains.Default(**kwargs)
        self.maxHealth = maxHealth
        self.maxEnergy = maxEnergy

        self.energy = maxEnergy
        self.health = self.maxHealth
        self.position = 0
        self.name = name
        self.board = None
        self.run_n = 0
        self.history = defaultdict()

    def die(self):
        print("%s has died at tile %d/%d"
            % (self.name, self.position, len(self.board.tiles)))
        

    def alive(self):
        return bool(max(0, self.health)) # If health is <= 0 then False

    def network(self, x):
        # y = np.random.choice([True, False]) # Placeholder for NN (coin flip)

        return y

    def reset(self):
        self.health = self.default_health
        self.position = 0
        self.history[self.run_n][self.position][health] = self.health
        self.history[self.run_n][self.position][tile] = (
            self.board.tiles[self.position])

    def run(self):
        for tile in self.board.tiles:
            self.position += 1
            self.history[run_n][self.position][health] = self.health
            block_damage = self.network(tile)
            if block_damage == False: self.health += tile

            if self.health < 0:
                self.die()
                break

        else:
            print("%s has survived all %d tiles with %f health" 
                    % (self.name, self.position, self.health))


if __name__ == '__main__':
    bob = Default()
    bob.brain.print_network()
    input('Done')