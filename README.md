# ACO-TSP

A Python implementation of the Ant Colony Optimization (ACO) metaheuristic for solving the Traveling Salesman Problem (TSP). This repository provides a modular, object-oriented solver with TSPLIB support, dynamic node handling, pheromone management, and plotting utilities.

## Features

- **Dynamic Node Support**  
  Automatically handles any number of cities: just load your `.tsp` file and the solver adapts to compute a tour over _n_ nodes.

- **TSPLIB Integration**  
  Load instances from `data/tsp/` or directly via URL.

- **Modular Design**  
  - `TSPInstance` for loading and distance-matrix computation  
  - `PheromoneMatrix` for evaporation & deposit  
  - `Ant` for probabilistic path construction  
  - `Colony` for iterating all ants  
  - `ACOSolver` for the full optimization loop  

- **Visualization**  
  Plot node coordinates and the best tour with Matplotlib.

- **Configurable**  
  Tune number of ants, iterations, α/β parameters, and evaporation rate.

## Formulas

### Next-City Probability

The probability that an ant at city _i_ moves to city _j_ is

$$
P_{ij}
\=\
\frac{\tau_{ij}^{\alpha}\,\eta_{ij}^{\beta}}
     {\displaystyle\sum_{k \in \mathrm{unvisited}}
       \tau_{ik}^{\alpha}\,\eta_{ik}^{\beta}}
\quad\text{where}\quad
\eta_{ij} = \frac{1}{d_{ij}}
$$

- $$\tau_{ij}\$$ = pheromone on edge (i,j)  
- $$\eta_{ij}\$$ = heuristic (inverse distance)  
- $$\alpha\$$ = pheromone influence  
- $$\beta\$$ = heuristic influence  

### Pheromone Update

After each iteration, pheromone on edge (i,j) is updated as:

$$
\tau_{ij}(t+1) \\leftarrow\ (1 - \rho)\\tau_{ij}
  \+\ \sum_{k=1}^{m} \Delta\tau_{ij}^{(k)},
$$

with

$$
\Delta\tau_{ij}^{(k)} =
\begin{cases}
\dfrac{Q}{L_{k}}, & \text{if ant }k\text{ used edge }(i,j),\\
0 & \text{otherwise},
\end{cases}
$$

- $$\rho\$$ = evaporation rate  
- $$Q$$ = pheromone constant (often 1)  
- $$L_{k}$$ = length of ant _k_’s tour  
- $$m$$ = number of ants  

## Installation

```bash
git clone https://github.com/mert1996/ACO-TSP.git
