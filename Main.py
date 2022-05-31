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

NOTE: To perform the search, the algorithm can only handle up to DATASIZE (num of cities) = 9 
      Anything higher will not perform well.

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


This will take (n!) amount of time. Therefore this will scale dramatically as we increase the amount of cities.
Whether it's finding the optimal solution or finding a solution, it will take (n!) amount of time.


This uses a queue to help traverse nodes for BFS.

Note: The algorithm created in this assignment, is designed in a fashion where we find the optimal solution.
"""
print("Pathfinding - Breadth-First Search")
BFS_path, BFS_distance = tsp.breadth_first_search()
print("Path:", BFS_path, "\nMinimum Distance:", BFS_distance)
#draw_graph(BFS_path, citiesList, "Breadth-First Search")
#
print()
#
"""
Depth-First Search (DFS)

In this algorithm, DFS performed well. The algorithm is designed in a way where, the path it takes (in this case), 
_will always traverse to the left side of the tree. And will keep traversing down the tree till we reach a leaf node. 
Once we reach a leaf node, we will find a path. 

Because of how the tree is created, the number of cities selected, is equal to the height of the tree.
What this means is, to find a solution, this will take (n) amount of time.

To find an optimal solution, this will take (n!) time. This is because we must traverse through all nodes/paths, and reach
_a leaf node to find out the optimal solution


This uses recursion to replicate a stack.

Note: The algorithm created in this assignment, is designed in a fashion where we find the optimal solution.
"""
print("Pathfinding - Depth-First Search")
DFS_path, DFS_distance = tsp.depth_first_search()
print("Path:", DFS_path, "\nMinimum Distance:", DFS_distance)
#draw_graph(DFS_path, citiesList, "Depth-First Search")
#
print()
#
"""
A* Search

In this algorithm, A* performed well. The algorithm is designed where we search through nodes, given a root node,
_and evaluates each children and their distance. We will determine their distance, and heuristic. We then store these 
_values into a tuple and push it into a priority queue.

The g() cost function used is the total distance traveled from the start node, to the current node
The h() cost function used is the Euclidean distance from the start node, to the current node
The f() cost function is the sum of g() and h()


This works similar to the Uniform Cost Search, as we have a priority queue.
The difference is, we sort the priority queue in ascending order by the f() cost value

The goal of the heuristic is to help the algorithm determine if we are getting close to our destination.


"""
print("Pathfinding - A* Search")
ASTAR_path, ASTAR_distance = tsp.a_star_search()
print("Path:", ASTAR_path, "\nMinimum Distance:", ASTAR_distance)
#draw_graph(ASTAR_path, citiesList, "A* Search")
