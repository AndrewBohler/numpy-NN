import numpy as np
import warnings
import os
from collections import defaultdict


def sigmoid(x):
    # standard activation function
    return 1 / (1+np.exp(-x))


def dSigmoid(x):
    # derivative of sigmoid
    return np.exp(-x)/((1+np.exp(-x))**2)


class Default(object):
    #goals = {'Live': }
    def __init__(self, iNeurons=1, hNeurons=3, oNeurons=1, n_layers=3,
        back_prop_rate=10, learning_rate=0.01):
        """
        :param iNeurons: x number of input neurons where x > 0
        :param hNeurons: x number of hidden neurons where x > 0
        :param oNeurons: x number of output neurons where x > 0
        :param n_layers: x number of layers where x >= 3
        :param back_prop_rate: number of forward passes in a minibatch
        :param learning_rate: augments dJdW applied to weights in back_prop()
        """
        self.iNeurons = int(iNeurons)
        self.hNeurons = int(hNeurons)
        self.oNeurons = int(oNeurons)
        self.n_layers = int(n_layers)
        self.back_prop_rate = back_prop_rate
        if learning_rate > 0:
            self.learning_rate = float(learning_rate)
        else:
            warnings.warn('Warning: learning_rate <= 0, using 0.01 instead')
            self.learning_rate = 0.01
        # assert default values or greater
        if self.iNeurons < 1:
            warnings.warn('Warning: iNeurons must be an int > 0\
                \nSetting iNeurons to 1')
            self.iNeurons = 1
        if self.hNeurons < 1:
            warnings.warn('Warning: hNeurons must be an int > 0\
                \nSetting iNeurons to 1')
            self.hNeurons = 1
        if self.n_layers < 3:
            warnings.warn('Warning: n_layers must be >= 3\
                \nSetting n_layers to 3')
            self.n_layers = 3
        # construct network, note that because we are using lists
        # everything starts at 0 so...
        # z[0] = a[0]*w[0] + b[0] and a[1] = sigmoid(z[0])
        self.a = [None] * self.n_layers
        self.w = [None] * (self.n_layers-1) # self.n_layers-1 because the
        self.b = [1.0] * (self.n_layers-1) # output has no w, b, z, or dJdW
        self.z = [None] * (self.n_layers-1)
        self.dJdW = [None] * (self.n_layers-1)
        # shape activation layers
        self.a[0] = np.ones((1, self.iNeurons))
        for i in range(1, self.n_layers-1):
            self.a[i] = np.zeros((1, self.hNeurons))
        self.a[self.n_layers-1] = np.zeros((1, self.oNeurons))
        # shape weights
        for i in range(len(self.w)):
            self.w[i] = np.ones((self.a[i].shape[1], self.a[i+1].shape[1]))
        # shape activity layers
        for i in range(self.n_layers-1):
            self.z[i] = np.zeros_like(self.a[i+1])
        # shape dJdW same as weights
        for i in range(self.n_layers-1):
            self.dJdW[i] = np.zeros_like(self.w[i])
        self.reset_weights()
        self.ioHistory = []

    def reset_weights(self):
        for i, weights in enumerate(self.w):
            self.w[i] = np.random.standard_normal(weights.shape)

    def feed_forward(self, inputs):
        """
        needs better formatting so the order doesn't matter
        :param inputs: ordered list of inputs
        """
        # set missing inputs to 0
        for i in range(self.iNeurons):
            try:
                self.a[0][0][i] = inputs[i]
            except TypeError as error:
                print(error, ', using 0 instead of input[{}]'.format(i))
                self.a[0][0][i] = 0
            except Exception as error:
                print(error, ', using 0 instead of input[{}]'.format(i))
                self.a[0][0][i] = 0
        # run through network: sigmoid(z=(a*w + b))
        for i in range(self.n_layers-1):
            self.z[i] = self.a[i].dot(self.w[i]) + self.b[i]
            self.a[i+1] = sigmoid(self.z[i])
        self.ioHistory.append((self.a[0], self.a[-1]))

    def cost(self, y, y_hat):
        return -(y-y_hat)


    def loss(self):
        pass


    def back_prop(self):
        """ Uses gradient decent to update weights """
        self.dJdW[-1] = np.multiply(-(self.a[0]-self.a[-1]), dSigmoid(self.z[-1]))

    def print_network(self):
        print('\niNeurons:', self.iNeurons,
        '\nhNeurons:', self.hNeurons,
        '\noNeurons:', self.oNeurons,
        '\nn_layers:', self.n_layers)
        print('\n   Network')
        for i in range(self.n_layers):
            try:
                print('_____________\n\n',
                    'activation[{}]:\n{}'.format(i, self.a[i]))
                print('_____________\n\n',
                    'weights[{}]:\n{}'.format(i, self.w[i]))
                print('_____________\n\n',
                    'bias[{}]: {}'.format(i, self.b[i]))
                print('_____________\n\n',
                    'activity[{}]:\n{}'.format(i, self.z[i]))
            except IndexError:
                print('_____________\n')
    
    def run(self, verbose=0):
        for i in range(self.back_prop_rate):
            self.feed_forward([13, 23, 16, 30])
            # if verbose >= 2:
            #     print(' input   output')
            #     print(self.ioHistory)
            #     for n, x, y in self.iNeurons, self.ioHistory[-1][0], self.ioHistory[-1][1]:
            #         print(' %4d  | %4d' % (x[0][n], y[0][n]))
            if verbose >= 1:
                print('Loss = {}'.format(self.loss))
        self.back_prop()
        



if __name__ =='__main__':
    brain = Default(iNeurons=4, oNeurons=4)
    brain.print_network
    while True:
        brain.run(verbose=2)
        brain.print_network()
        print('Loss = {}'.format(brain.loss))
        user_input = input('Continue?')
        if user_input == '' or 'y' or 'yes':
            continue
        else:
            break
1
234
5
54
6


    input('End of code')