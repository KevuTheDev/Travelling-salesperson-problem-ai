import math

class State:
    def __init__(self, p_name, p_latitude, p_longitude):
        self.m_name = p_name
        self.m_latitude = p_latitude
        self.m_longitude = p_longitude

        return

    def __str__(self):
        return f"{self.m_name:<12} {self.m_latitude:<10} {self.m_longitude:<12}"
        # return "N:" + self.m_name + ", LA:" + str(self.m_latitude) + ", LO:" + str(self.m_longitude)

# Prints States
# param: statesList <Array of State Objects>
def PrintStates(p_stateList):
    print("State        Latitude   Longitude\n")
    for i in p_stateList:
        print(i)
    return

# Calculates and returns Euclidean Distance
# param: x <State Object>, y <State Object>
# return: distance <float>
def EuclideanDistance(p_x, p_y):
    a = math.pow(p_x.m_latitude - p_y.m_latitude, 2)
    b = math.pow(p_x.m_longitude - p_y.m_longitude, 2)

    return math.sqrt(a + b)

def GenerateDistanceMatrix(p_statesList):
    dMatrix = []
    for ci, i in enumerate(p_statesList):
        dMatrix.append([])
        for cj, j in enumerate(p_statesList):
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



