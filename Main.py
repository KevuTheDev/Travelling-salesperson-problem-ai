import pandas as pd

from Utils import *
from TSP import *
from Tree import *



DATASIZE = 10  #YOUR SIZE



data = pd.read_csv("data/city_data_50.csv", index_col=None, header=0, engine='python')
data = data.values.tolist()

data = data[:DATASIZE]
citiesList = GenerateCitiesList(data)
PrintCities(citiesList)

distanceMatrix = GenerateDistanceMatrix(citiesList)
print("="*30)
print("Rows are source")
print("Columns are destination")
PrintDistanceMatrix(distanceMatrix)
#
# TREE = Tree(distanceMatrix)
# TREE.create_tree()
# print(TREE.m_height, DATASIZE)


print()

tsp = TSP(distanceMatrix)

print("Pathfinding - Breath-First Search")
BFS_path, BFS_distance = tsp.TSP_BFS()
print("Path:",BFS_path, "\nMinimum Distance:",BFS_distance)
DrawGraph(BFS_path, citiesList, "Breath-First Search")
#
print()
#
print("Pathfinding - Depth-First Search")
DFS_path, DFS_distance = tsp.TSP_DFS()
print("Path:",DFS_path, "\nMinimum Distance:",DFS_distance)
DrawGraph(DFS_path, citiesList, "Depth-First Search")
#
print()
#
print("Pathfinding - Minimum Spanning Tree Search")
MST_path, MST_distance = tsp.TSP_MST(0)
print("Path:",MST_path, "\nMinimum Distance:",MST_distance)
DrawGraph(MST_path, citiesList, "Minimum Spanning Tree Search")
#
print()
#
print("Pathfinding - Brute Force Search")
BFM_path, BFM_distance = tsp.TSP_BruteForce(0)
print("Path:",BFM_path, "\nMinimum Distance:",BFM_distance)
DrawGraph(BFM_path, citiesList, "Brute Force Search")