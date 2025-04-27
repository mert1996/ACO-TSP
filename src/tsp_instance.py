import tsplib95
import numpy as np


class TSPInstance:
    def __init__(self, problem_codename):
        self.problem = tsplib95.load(f'./data/tsp/{problem_codename}.tsp')
        if "node_coords" in self.problem.as_name_dict().keys():
            coords = self.problem.as_name_dict()["node_coords"]
            self.nodes = {i: coords[i] for i in sorted(coords)}
            self.n = len(self.nodes)
            self.dist_matrix = self._compute_dist_matrix()
        else:
            raise ValueError(f"No 'node_coords' key for {problem_codename}")

    def _compute_dist_matrix(self):
        dm = np.zeros((self.n, self.n))
        for i, (ix, iy) in self.nodes.items():
            for j, (jx,jy) in self.nodes.items():
                dm[i-1,j-1] = np.hypot(ix-jx, iy-jy)
        return dm
