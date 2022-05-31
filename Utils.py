from math import pow, sqrt
# from matplotlib import pyplot as plt
from City import *


def generate_cities_list(p_data):
    """
    Generates States Object List given a 2d list of data
    :param p_data: <List of List containing tokenized csv data
    :return: sList [List of City Object]
    """
    sList = []
    for i in p_data:
        s = City(i[0], i[2], i[3])
        sList.append(s)
    return sList


def print_cities(p_citiesList):
    """
    Prints Cities
    :param p_citiesList: Array of City Objects
    :return:
    """
    print("State        Latitude   Longitude\n")
    for i in p_citiesList:
        print(i)
    return


def euclidean_distance(p_x, p_y):
    """
    Calculates and returns Euclidean Distance
    :param p_x: City Object
    :param p_y: City Object
    :return: distance (float)
    """
    a = pow(p_x.m_latitude - p_y.m_latitude, 2)
    b = pow(p_x.m_longitude - p_y.m_longitude, 2)

    return sqrt(a + b)


def generate_distance_matrix(p_citiesList):
    """
    Generates a distance Matrix where each cell represents the euclidean distance from the row index and the column index
    Each index from row and column, represents the index in the provided p_citiesList
    :param p_citiesList: List of City Objects
    :return: a distance Matrix (2D List of floats)
    """
    dMatrix = []
    for ci, i in enumerate(p_citiesList):
        dMatrix.append([])
        for cj, j in enumerate(p_citiesList):
            d = euclidean_distance(i, j)
            dMatrix[ci].append(d)

    return dMatrix


def print_distance_matrix(p_distanceMatrix):
    """
    Prints a formatted distance matrix, given a distance Matrix
    :param p_distanceMatrix: 2D list of floats
    :return: None
    """
    print("     ", end="")
    for i in range(len(p_distanceMatrix)):
        print(f"{i:<8}", end=" ")
    print()

    for index, row in enumerate(p_distanceMatrix):
        print(f"{index}", end="    ")
        for i in row:
            print(f"{i:<8.3f}", end=" ")
        print()

    return


def distance_matrix_to_csv(p_distanceMatrix):
    """
    This prints into console, a distance matrix in a csv (comma-seperated values) for visual purposes
    :param p_distanceMatrix:
    :return:
    """
    print(end=",")

    for i in range(len(p_distanceMatrix)):
        print(i, end=",")
    print()

    for ci, i in enumerate(p_distanceMatrix):
        print(ci, end=",")
        for j in i:
            print(j, end=",")
        print()


# def draw_graph(p_pathList, p_citiesList, p_title):
#     """
#     This will draw a graph using matplotlib.
#     Prints a graph to display the route of the graph
#     :param p_pathList: A list on integers, representing cities
#     :param p_citiesList: A list of City Objects
#     :param p_title: A string for the title of the image
#     :return: None
#     """
#     if p_pathList is None:
#         return
#
#     plt.rcParams["figure.figsize"] = [10, 8]
#     plt.rcParams["figure.autolayout"] = True
#     fig = plt.figure()
#     ax = fig.add_subplot()
#
#     for ci, i in enumerate(p_pathList):
#         if ci == 0:
#             x = i
#         else:
#             plt.text(p_citiesList[i].m_latitude + 0.35, p_citiesList[i].m_longitude, str(i), ha='left', size=12,
#                      color='blue')
#
#             y = i
#
#             latitude = [p_citiesList[x].m_latitude, p_citiesList[y].m_latitude]
#             longitude = [p_citiesList[x].m_longitude, p_citiesList[y].m_longitude]
#
#             ax.plot(latitude, longitude, color='black')
#             ax.scatter(latitude, longitude, c='red', s=100)
#
#             x = y
#     plt.title(p_title)
#
#     plt.show()
#     return


def create_unvisited_list(p_path, p_size):
    """
    This is a utility function used to create a list of integers

    This function will compare 2 different lists, the given p_path, and a list from 0 to p_size
    We will remove items from the new list, that are already in the p_path list.

    We then return the new list, that have been stripped.

    :param p_path: List of Integers
    :param p_size: The number of cities
    :return: A list with no values similar to p_path
    """
    unvisitedList = [i for i in range(p_size)]

    for i in p_path:
        unvisitedList.remove(i)

    return unvisitedList


def a_star_binary_search_insert(p_arr, p_x):
    """
    **THIS IS FOR A* SEARCH ONLY**
    A binary search insert algorithm, where we will insert objects while using a binary search method.
    this will efficiently insert nodes into a given list
    :param p_arr:
    :param p_x:
    :return:
    """
    return a_star_binary_search_insert_aux(p_arr, 0, len(p_arr) - 1, p_x)


def a_star_binary_search_insert_aux(p_arr, p_low, p_high, p_x):
    """
    Auxilary function for a_star_binary_search_insert

    This is recursive

    :param p_arr: The array of FORMAT(currentNode, path, distance, AStarDistance)
    :param p_low: int value of the lower bound
    :param p_high: int value of the higher bound
    :param p_x: the given value, that will be inserted into the list
    :return: None
    """
    if p_high >= p_low:
        mid = (p_high + p_low) // 2

        if p_arr[mid][3] == p_x[3]:
            p_arr.insert(mid, p_x)
            return mid

        elif p_arr[mid][3] > p_x[3]:
            return a_star_binary_search_insert_aux(p_arr, p_low, mid - 1, p_x)

        else:
            return a_star_binary_search_insert_aux(p_arr, mid + 1, p_high, p_x)

    else:
        p_arr.insert(p_low, p_x)
        return