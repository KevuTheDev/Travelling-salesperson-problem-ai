import pandas as pd
from Utils import *
from TSP import *

DATASIZE = 9  # YOUR SIZE



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
#
# TREE = Tree(distanceMatrix)
# TREE.create_tree()
# print(TREE.m_height, DATASIZE)


print()

tsp = TSP(distanceMatrix)
# print(tsp.TSP_ASTAR(distanceMatrix, 0, len(distanceMatrix)))

print("Pathfinding - Breath-First Search")
BFS_path, BFS_distance = tsp.breadth_first_search()
print("Path:", BFS_path, "\nMinimum Distance:", BFS_distance)
#draw_graph(BFS_path, citiesList, "Breath-First Search")
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
#
print()
#
print("Pathfinding - Minimum Spanning Tree Search")
MST_path, MST_distance = tsp.TSP_MST(0)
print("Path:", MST_path, "\nMinimum Distance:", MST_distance)
#draw_graph(MST_path, citiesList, "Minimum Spanning Tree Search")
#
print()

print("Pathfinding - Brute Force Search")
BFM_path, BFM_distance = tsp.TSP_BruteForce(0)
print("Path:", BFM_path, "\nMinimum Distance:", BFM_distance)
#draw_graph(BFM_path, citiesList, "Brute Force Search")
