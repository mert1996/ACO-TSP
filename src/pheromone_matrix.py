import numpy as np


class PheromoneMatrix:
    def __init__(self, n, init_pher=1.0, evap_rate=0.5):
        self.n = n
        self.evap_rate = evap_rate
        self.matrix = np.full((n,n), init_pher)

    def evaporate(self):
        self.matrix *= (1 - self.evap_rate)

    def deposit(self, tours):
        for tour, length in tours:
            for a, b in zip(tour[:-1], tour[1:]):
                i, j = a-1, b-1
                self.matrix[i, j] += 1.0/length
                self.matrix[j, i] += 1.0/length
