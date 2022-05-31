"""
Assignment #1

Kevin He
181803930 / hexx3930
hexx3930@mylaurier.ca


"""

import pandas as pd
from Utils import *
from TSP import *

DATASIZE = 9  # YOUR SIZE and number of cities



data = pd.read_csv("data/city_data_50.csv", index_col=None, header=0, engine='python')
data = data.values.tolist()

data = data[:DATASIZE]
citiesList = generate_cities_list(data)
print_cities(citiesList)

distanceMatrix = generate_distance_matrix(citiesList)
print("=" * 30)
print("Rows are source")
print("Columns are destination")
print_distance_matrix(distanceMatrix)
print()

"""
The Travelling Salesperson Problem (TSP)

The goal of this problem is to travel through every city at most once, and to be able to return back to the starting point.
We will be using three different algorithms to analyze how they perform in this problem. 

1) Breadth-First Search (BFS)
2) Depth-First Search (DFS)
3) A* Search

To perform the search, the algorithm can only handle up to DATASIZE (num of cities) 



"""
tsp = TSP(distanceMatrix)
"""
Breadth-First Search (BFS)

In this algorithm, BFS had a rough time performing. This took a long time due to how the algorithm worked.
The algorithm works by starting at a root node, then check all its children nodes.
We store each children node into a queue, and loop until we reach a node where they don't have any children (a leaf node)
_which represents the completion of a path
 
As you can see, this is not an optimal solution. The algorithm has to search from every node at every height of the tree 
_before we find a solution.



"""
print("Pathfinding - Breadth-First Search")
BFS_path, BFS_distance = tsp.breadth_first_search()
print("Path:", BFS_path, "\nMinimum Distance:", BFS_distance)
#draw_graph(BFS_path, citiesList, "Breadth-First Search")
#
print()
#
print("Pathfinding - Depth-First Search")
DFS_path, DFS_distance = tsp.depth_first_search()
print("Path:", DFS_path, "\nMinimum Distance:", DFS_distance)
#draw_graph(DFS_path, citiesList, "Depth-First Search")
#
print()
#
print("Pathfinding - A* Search")
ASTAR_path, ASTAR_distance = tsp.a_star_search()
print("Path:", ASTAR_path, "\nMinimum Distance:", ASTAR_distance)
#draw_graph(ASTAR_path, citiesList, "A* Search")
