from itertools import permutations
from sys import maxsize as MAXSIZE
from Tree import *
from Utils import a_star_binary_search_insert, create_unvisited_list


class TSP:
    def __init__(self, p_distanceMatrix):
        """
        Initialization of the TSP class
        :param p_distanceMatrix: 2D list of floats
        """
        self.m_distanceMatrix = p_distanceMatrix
        self.m_tree: Tree = None
        self.m_minimumPath = []
        self.m_minimumDistance = MAXSIZE

        self.create_tree()

    def reset_state(self):
        """
        Reset class members that are used to retain information while
        Depth-first search and Breadth-first search is running
        :return: None
        """
        self.m_minimumPath = []
        self.m_minimumDistance = MAXSIZE

    def create_tree(self):
        """
        Private function that will run when the TSP class is instantiated
        It is used to create a Tree used for traversal of BFS and DFS
        :return: None
        """
        print("Generating Tree...")
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

    def depth_first_search(self):
        """
        **This algorithm was designed to find the optimal solution.**

        In this algorithm, we are trying to perform a depth first search.
        This algorithm will perform the search on a generated tree structure. self.create_tree()

        :return: (List[int]): the resulting minimum path, (float): the resulting minimum distance found
        """
        self.reset_state()
        currentNode = self.m_tree.root()

        if currentNode is None:
            return None, None

        self.depth_first_search_aux(currentNode, 0, [currentNode.data()])

        return self.m_minimumPath, self.m_minimumDistance

    def depth_first_search_aux(self, p_previous: Node, p_distance: int, p_path):
        """
        This is an auxiliary function for the depth-first search.

        :param p_previous: the previous node
        :param p_distance: the previous distance
        :param p_path: the previous path
        :return: None
        """
        newPath = []
        newDistance = p_distance

        # This is where we apply a recursive function and a for loop
        # the for-loop is used to search through every unvisited node in this path
        # the recursive function is used to back-track after reaching a leaf
        # Note: It is designed to find optimal
        for i in p_previous.m_nodeList:
            newPath = [i for i in p_path]  # Avoiding deepcopy for some efficiency
            newDistance = p_distance
            newDistance += self.m_distanceMatrix[p_previous.data()][i.data()]
            newPath.append(i.data())
            self.depth_first_search_aux(i, newDistance, newPath)

        # When reached at the leaf node, perform a calculation to determine whether if this path is shorter
        # than the stored path. If so store a copy of the solution.
        if len(p_previous.m_nodeList) == 1:
            lastNode = p_previous.m_nodeList[-1]
            newDistance += self.m_distanceMatrix[lastNode.data()][self.m_tree.root().data()]
            newPath.append(self.m_tree.root().data())

            if newDistance < self.m_minimumDistance:
                self.m_minimumDistance = newDistance
                self.m_minimumPath = [i for i in newPath]

    def breadth_first_search(self):
        """
        **This algorithm was designed to find the optimal solution.**


        In this algorithm, we are trying to perform a breadth-first search
        This algorithm will perform the search on a generated tree structure. self.create_tree()

        :return: (List[int]): the resulting minimum path, (float): the resulting minimum distance found
        """
        self.reset_state()
        nodeListQueue = []  # FORMAT(NODE, path, distance) stored in Queue
        currentNode = self.m_tree.root()

        if currentNode is None:
            return None, None

        for i in currentNode.m_nodeList:
            # FORMAT(NODE, path, distance)
            path = [currentNode.data(), i.data()]
            distance = self.m_distanceMatrix[currentNode.data()][i.data()]
            nodeListQueue.append((i, path, distance))

        # This is the loop to search every node
        # We are completing the queue because its goal is to find optimal route
        while len(nodeListQueue) != 0:
            current = nodeListQueue.pop(0)  # FORMAT(NODE, path, distance)

            currentNode = current[0]
            if len(currentNode.m_nodeList) != 0:
                # Given a node, search through each children at this node, and store it into the queue
                for i in currentNode.m_nodeList:
                    path = [i for i in current[1]]
                    path.append(i.data())
                    distance = current[2] + self.m_distanceMatrix[currentNode.data()][i.data()]
                    nodeListQueue.append((i, path, distance))
            else:
                # When we reach a leaf node, we calculate and evaluate if a path is shorter than the currently
                # stored one. If so replace it
                startNode = self.m_tree.root()
                distance = current[2] + self.m_distanceMatrix[currentNode.data()][startNode.data()]
                if distance < self.m_minimumDistance:
                    self.m_minimumDistance = distance
                    self.m_minimumPath = [i for i in current[1]]
                    self.m_minimumPath.append(self.m_tree.root().data())

        return self.m_minimumPath, self.m_minimumDistance

    def a_star_search(self):
        """
        **This algorithm is not an optimal A* algorithm as it is not using the best heuristic (i think)**

        In this algorithm, we are trying to perform an a* search.
        We will not be traversing through a tree data structure.


        The g() cost function used is the total distance traveled from the start node, to the current node
        The h() cost function used is the Euclidean distance from the start node, to the current node
        The f() cost function is the sum of g() and h()

        The priority queue used, is sorted in ascending order of the h() cost
        We used a binary insertion for inserting into the priority queue, to speed up the process.

        This will return the first path the algorithm has found.

        :return: (List[int]): the resulting minimum path, (float): the resulting minimum distance found
        """
        p_distanceMatrix = self.m_distanceMatrix
        p_startNode = 0
        p_size = len(self.m_distanceMatrix)
        nodeListPriorityQueue = []  # FORMAT(currentNode, path, distance, AStarDistance)

        ccItem = (p_startNode, [p_startNode], 0, 0)
        nodeListPriorityQueue.append(ccItem)

        # Looping through the whole priority queue
        # But it will terminate when we find an answer
        while len(nodeListPriorityQueue) != 0:
            # FORMAT(currentNode, path, distance, AStarDistance)

            #Pop the first node from the priority queue
            cItem = nodeListPriorityQueue.pop(0)
            unvisited = create_unvisited_list(cItem[1], p_size) #creating an array of unvisited nodes

            # If there are more unvisited nodes for this path, continue adding more nodes into the priority queue
            if len(unvisited) != 0:
                for i in unvisited:
                    newPath = [x for x in cItem[1]]
                    newPath.append(i)

                    newDistance = cItem[2] + p_distanceMatrix[cItem[0]][i]  # g(x)
                    newAStarDistance = newDistance + p_distanceMatrix[i][p_startNode]  # f() = g() + h()
                    newItem = (i, newPath, newDistance, newAStarDistance)
                    a_star_binary_search_insert(nodeListPriorityQueue, newItem)
            else:
                # If no more nodes in unvisited list, determine if the node is not the starting node

                # if it isn't the starting node, update the node, as it has reached the final
                # destination and completed the loop
                if cItem[0] != p_startNode:
                    newPath = [x for x in cItem[1]]
                    newDistance = cItem[2] + p_distanceMatrix[cItem[0]][p_startNode]  # g(x)
                    newAStarDistance = newDistance  # f() = g() + h()
                    newItem = (p_startNode, newPath, newDistance, newAStarDistance)
                    a_star_binary_search_insert(nodeListPriorityQueue, newItem)

                # if this is the starting node, then this is our answer as it has already completed the path
                else:
                    newPath = cItem[1]
                    newPath.append(p_startNode)
                    return newPath, cItem[2]


