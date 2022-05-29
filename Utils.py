from math import pow, sqrt
from matplotlib import pyplot as plt

from City import *


# Generates States Object List given a 2d list of data
# param: p_data <List of List containing tokenized csv data
# return: sList <List of State Object>
def GenerateCitiesList(p_data):
    sList = []
    for i in p_data:
        s = City(i[0], i[2], i[3])
        sList.append(s)
    return sList


# Prints City
# param: statesList <Array of State Objects>
def PrintCities(p_citiesList):
    print("State        Latitude   Longitude\n")
    for i in p_citiesList:
        print(i)
    return


# Calculates and returns Euclidean Distance
# param: x <State Object>, y <State Object>
# return: distance <float>
def EuclideanDistance(p_x, p_y):
    a = pow(p_x.m_latitude - p_y.m_latitude, 2)
    b = pow(p_x.m_longitude - p_y.m_longitude, 2)

    return sqrt(a + b)


def GenerateDistanceMatrix(p_citiesList):
    dMatrix = []
    for ci, i in enumerate(p_citiesList):
        dMatrix.append([])
        for cj, j in enumerate(p_citiesList):
            d = EuclideanDistance(i, j)
            dMatrix[ci].append(d)

    return dMatrix


def PrintDistanceMatrix(p_distanceMatrix):
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


def DistanceMatrixToCSV(p_distanceMatrix):
    print(end=",")

    for i in range(len(p_distanceMatrix)):
        print(i, end=",")
    print()

    for ci, i in enumerate(p_distanceMatrix):
        print(ci, end=",")
        for j in i:
            print(j, end=",")
        print()


# Given an array of indices representing a path, and given an array of States...
# draw a graph
def DrawGraph(p_pathList, p_citiesList, p_title):

    if p_pathList is None:
        return

    plt.rcParams["figure.figsize"] = [10, 8]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot()

    for ci, i in enumerate(p_pathList):
        if ci == 0:
            x = i
        else:
            plt.text(p_citiesList[i].m_latitude + 0.35, p_citiesList[i].m_longitude, str(i), ha='left', size=12,
                     color='blue')

            y = i

            latitude = [p_citiesList[x].m_latitude, p_citiesList[y].m_latitude]
            longitude = [p_citiesList[x].m_longitude, p_citiesList[y].m_longitude]

            ax.plot(latitude, longitude, color='black')
            ax.scatter(latitude, longitude, c='red', s=100)

            x = y
    plt.title(p_title)

    plt.show()
    return