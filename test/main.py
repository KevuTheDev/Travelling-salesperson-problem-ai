# Import pandas
import pandas as pd
import math
from copy import deepcopy
from itertools import permutations
from sys import maxsize


class Node:
    def __init__(self, p_data):
        self.m_data: int = p_data
        self.m_nodeList: [Node] = []

    def __str__(self):
        return str(self.m_data)


class Tree:
    def __init__(self):
        self.m_root: Node = None

    def create_tree(self, p_data):
        item = p_data[0]
        p_data = p_data.replace(item, "")
        node = Node(int(item))

        self.m_root = node

        newData = (p_data + '.')[:-1]

        for i in newData:
            self.create_tree_aux(self.m_root, newData, i)

        return

    def create_tree_aux(self, currentNode, p_data, p_index):
        newData = (p_data + '.')[:-1]
        newData = newData.replace(p_index, "")
        node = Node(int(p_index))
        currentNode.m_nodeList.append(node)

        currentNode = node

        for i in newData:
            self.create_tree_aux(currentNode, newData, i)

        return

    def print_tree(self):
        currentNode = self.m_root
        print(currentNode)
        self.print_tree_aux(currentNode)

        return

    def print_tree_aux(self, p_node: Node):
        for i in p_node.m_nodeList:
            print(i, end=" ")
        print()

        for i in p_node.m_nodeList:
            self.print_tree_aux(i)
        return

    def TSP_DFS(self, p_startNode):
        currentNode = self.m_root




def create_string(p_size):
    myString = ""
    for i in range(p_size):
        myString += str(i)
    return myString


SIZE = 10
DATA = create_string(SIZE)

TREE = Tree()
TREE.create_tree(DATA)
i=1
#TREE.print_tree()


