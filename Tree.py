class Node:
    def __init__(self, p_data):
        self.m_data = p_data
        self.m_nodeList = []

    def __str__(self):
        return str(self.m_data)

    def data(self):
        return self.m_data

    def isempty(self):
        return len(self.m_nodeList) == 0


class Tree:
    def __init__(self, p_height):
        self.m_root = None
        self.m_height = p_height
        self.create_tree()

    def height(self):
        return self.m_height

    def root(self):
        return self.m_root

    def create_tree(self):
        if self.m_height == 0:
            return

        dataList = [i for i in range(self.m_height)]
        nodeValue = dataList[0]
        dataList.remove(nodeValue)
        node = Node(int(nodeValue))

        self.m_root = node

        newDataList = [i for i in dataList]

        for i in newDataList:
            self.create_tree_aux(self.m_root, newDataList, i)

    def create_tree_aux(self, p_currentNode, p_dataList, p_index):
        newDataList = [i for i in p_dataList]
        newDataList.remove(p_index)
        node = Node(int(p_index))
        p_currentNode.m_nodeList.append(node)

        currentNode = node

        for i in newDataList:
            self.create_tree_aux(currentNode, newDataList, i)
        return


def create_string(p_size):
    myString = ""
    for i in range(p_size):
        myString += str(i)
    return myString