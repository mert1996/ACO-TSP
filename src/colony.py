from .ant import Ant


class Colony:
    def __init__(self, num_ants, instance, pheromone, alpha, beta):
        self.ants = [Ant(instance.n, instance.dist_matrix, pheromone.matrix, alpha, beta) for _ in range(num_ants)]
        self.pheromone = pheromone

    def run_iteration(self):
        tours = []
        for ant in self.ants:
            ant.reset()
            t = ant.build_tour()
            tours.append((t, ant.tour_length()))
        self.pheromone.evaporate()
        self.pheromone.deposit(tours)
        return min(tours, key=lambda x: x[1])
