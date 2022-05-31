class Node:
    def __init__(self, p_data):
        """
        Initialization of class
        :param p_data: an integer number representing a City
        """
        self.m_data = p_data
        self.m_nodeList = []

    def __str__(self):
        """
        Output a string value
        :return: string value of data
        """
        return str(self.m_data)

    def data(self):
        """
        Output the value of the Node object
        :return: int value
        """
        return self.m_data


class Tree:
    def __init__(self, p_height):
        """
        Initialization of the Tree Object
        Will generate a tree data structure on initialization
        :param p_height: an int that represents how many cities
        """
        self.m_root = None
        self.m_height = p_height
        self.create_tree()

    def height(self):
        """
        Returns the height of the tree
        :return: (int) height
        """
        return self.m_height

    def root(self):
        """
        Returns the root node of the tree
        :return: (Node) root node
        """
        return self.m_root

    def create_tree(self):
        """
        Will Generate a tree data structure
        :return: None
        """
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
        """
        The create_tree auxiliary function used to help create a tree
        :param p_currentNode: (Node)
        :param p_dataList: (List of Integers)
        :param p_index: (int) Current number position
        :return: None
        """
        newDataList = [i for i in p_dataList]
        newDataList.remove(p_index)
        node = Node(int(p_index))
        p_currentNode.m_nodeList.append(node)

        currentNode = node

        for i in newDataList:
            self.create_tree_aux(currentNode, newDataList, i)
        return