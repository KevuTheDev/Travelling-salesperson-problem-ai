# Import pandas
import pandas as pd
import math
from copy import deepcopy
from itertools import permutations
from sys import maxsize


class Node:
    def __init__(self, p_data, p_left=None, p_right=None):
        self.m_data = p_data
        self.m_left = p_left
        self.m_right = p_right

    def __str__(self):
        return str(self.m_data)


class Tree:
    def __init__(self):
        self.m_root = None

    def create_tree(self):
        if self.m_root is None:
            self.m_root = Node(0)
        return
