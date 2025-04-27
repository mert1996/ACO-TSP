from .pheromone_matrix import PheromoneMatrix
from .colony import Colony


class ACOSolver:
    def __init__(self, instance, num_ants=10, iterations=100, alpha=1, beta=2, evap_rate=0.5):
        self.instance = instance
        self.pheromone = PheromoneMatrix(instance.n, evap_rate=evap_rate)
        self.colony = Colony(num_ants, instance, self.pheromone, alpha, beta)
        self.iterations = iterations

    def run(self):
        best_tour, best_len = None, float('inf')
        for _ in range(self.iterations):
            tour, length = self.colony.run_iteration()
            if length < best_len:
                best_tour, best_len = tour, length
        return best_tour, best_len
