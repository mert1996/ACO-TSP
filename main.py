from src.tsp_instance import TSPInstance
from src.aco_solver import ACOSolver
from src.plotting import plot_best_tour


def main():
    inst = TSPInstance('ulysses22')
    solver = ACOSolver(inst, num_ants=20, iterations=200, alpha=1, beta=5, evap_rate=0.3)
    tour, length = solver.run()
    print('Best tour:', tour)
    print('Length:', length)

    plot_best_tour(inst.nodes, tour, length)


if __name__ == '__main__':
    main()
