import numpy as np


class Ant:
    def __init__(self, n, dist_matrix, pheromone, alpha=1, beta=2):
        self.visited = None
        self.tour = None
        self.n = n
        self.dist = dist_matrix
        self.pher = pheromone
        self.alpha = alpha
        self.beta = beta
        self.reset()

    def reset(self):
        start = np.random.randint(1, self.n + 1)
        self.tour = [start]
        self.visited = {start}

    def select_next(self):
        current = self.tour[-1] - 1
        unv = [i for i in range(self.n) if i + 1 not in self.visited]
        probs = []

        for j in unv:
            tau = self.pher[current, j] ** self.alpha
            eta = (1.0 / (self.dist[current, j] + 1e-10)) ** self.beta
            probs.append(tau * eta)
        probs = np.array(probs)
        probs /= probs.sum()
        choice = np.random.choice(len(unv), p=probs)
        city = unv[choice] + 1
        self.tour.append(city)
        self.visited.add(city)

    def build_tour(self):
        while len(self.tour) < self.n:
            self.select_next()
        self.tour.append(self.tour[0])
        return self.tour

    def tour_length(self):
        total = 0
        for a,b in zip(self.tour[:-1], self.tour[1:]):
            total += self.dist[a-1, b-1]
        return total
