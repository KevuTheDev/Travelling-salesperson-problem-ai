from itertools import permutations
from sys import maxsize as MAXSIZE
from Tree import *


class TSP:
    def __init__(self, p_distanceMatrix):
        self.m_distanceMatrix = p_distanceMatrix
        self.m_tree: Tree = None
        self.m_minimumPath = []
        self.m_minimumDistance = MAXSIZE

        self.create_tree()

    def reset_state(self):
        self.m_minimumPath = []
        self.m_minimumDistance = MAXSIZE

    def create_tree(self):
        print("Creating Tree")
        self.m_tree = Tree(len(self.m_distanceMatrix))

    def TSP_BruteForce(self, s):
        if len(self.m_distanceMatrix) == 0:
            return None, None

        # store all vertex apart from source vertex
        vertex = []
        for i in range(len(self.m_distanceMatrix)):
            if i != s:
                vertex.append(i)

        # store minimum weight Hamiltonian Cycle
        min_path = MAXSIZE
        next_permutation = permutations(vertex)
        path = []

        for i in next_permutation:

            # store current Path weight(cost)
            current_pathweight = 0

            # compute current path weight
            k = s
            for j in i:
                current_pathweight += self.m_distanceMatrix[k][j]
                k = j
            current_pathweight += self.m_distanceMatrix[k][s]

            # update minimum
            if min(min_path, current_pathweight) != min_path:
                lpath = list(i)
                path = [i for i in lpath]
                min_path = min(min_path, current_pathweight)

        path = list(path)
        path.insert(s, 0)
        path.append(s)
        return path, min_path

    def TSP_MST(self, s):
        array = []
        size = len(self.m_distanceMatrix)

        if size == 0:
            return None, None

        unvisitedList = [i for i in range(size)]

        unvisitedList.remove(s)
        array.append(s)

        currentNode = s
        currentPathWeight = 0

        while len(unvisitedList) != 0:
            min_path = MAXSIZE
            min_node = -1

            for i in unvisitedList:
                if min(min_path, self.m_distanceMatrix[currentNode][i]) != min_path:
                    min_path = self.m_distanceMatrix[currentNode][i]
                    min_node = i

            currentNode = min_node
            currentPathWeight += min_path

            unvisitedList.remove(min_node)
            array.append(min_node)

        currentPathWeight += self.m_distanceMatrix[currentNode][s]
        array.append(s)

        return array, currentPathWeight

    def TSP_DFS(self):
        # size = 2

        # a min path is selected when we reached the end-of-a-path
        # an end-of-a-path, is when we reach a place where there is no more nodes to visit
        # we replace the current minPath & minDistance, when we reach end-of-a-path, and the distance of that path ...
        # is smaller than minDistance

        # the tree should be created during the creation of the TSP class
        self.reset_state()
        currentNode = self.m_tree.root()

        if currentNode is None:
            return None, None

        array = [currentNode.data()] # the path

        self.TSP_DFS_aux(currentNode, 0, array)

        return self.m_minimumPath, self.m_minimumDistance

    def TSP_DFS_aux(self, p_previous : Node, p_distance: int, p_path):
        newPath = []
        newDistance = p_distance

        for i in p_previous.m_nodeList:
            newPath = [i for i in p_path]
            newDistance = p_distance
            newDistance += self.m_distanceMatrix[p_previous.data()][i.data()]
            newPath.append(i.data())
            self.TSP_DFS_aux(i, newDistance, newPath)

        if len(p_previous.m_nodeList) == 1:
            lastNode = p_previous.m_nodeList[-1]
            newDistance += self.m_distanceMatrix[lastNode.data()][self.m_tree.root().data()]
            newPath.append(self.m_tree.root().data())

            if newDistance < self.m_minimumDistance:
                self.m_minimumDistance = newDistance
                self.m_minimumPath = [i for i in newPath]

    def TSP_BFS(self):
        self.reset_state()
        nodeListQueue = []
        currentNode = self.m_tree.root()

        if currentNode is None:
            return None, None

        for i in currentNode.m_nodeList:
            # (NODE, path, distance)
            path = [currentNode.data(), i.data()]
            distance = self.m_distanceMatrix[currentNode.data()][i.data()]
            nodeListQueue.append((i, path, distance))

        while len(nodeListQueue) != 0:
            current = nodeListQueue.pop(0) # (NODE, path, distance)


            currentNode = current[0]
            if len(currentNode.m_nodeList) != 0:
                for i in currentNode.m_nodeList:
                    path = [i for i in current[1]]
                    path.append(i.data())
                    distance = current[2] + self.m_distanceMatrix[currentNode.data()][i.data()]
                    nodeListQueue.append((i, path, distance))
            else:
                startNode = self.m_tree.root()
                distance = current[2] + self.m_distanceMatrix[currentNode.data()][startNode.data()]
                if distance < self.m_minimumDistance:
                    self.m_minimumDistance = distance
                    self.m_minimumPath = [i for i in current[1]]
                    self.m_minimumPath.append(self.m_tree.root().data())

        return self.m_minimumPath, self.m_minimumDistance

    def TSP_ASTAR(self):
        self.reset_state()
        nodeListPriorityQueue = []
        currentNode = self.m_tree.root()





        return self.m_minimumPath, self.m_minimumDistance
