#TODO: Typowanie

"""
Node vs Vertex
"""

class Vertex():
    def __init__(self, key):
        self.id = key
        self.neighbours = {}

    def addNeighbour(self, neighbour, weight=0):
        self.neighbours[neighbour] = weight
    
    def getConnections(self):
        return self.neighbours.keys()

    def getId(self):
        return self.id
    
    def getWeight(self, neighbour):
        return self.neighbours[neighbour]

    def __str__(self) -> str:
        return str(self.id) + ' connected to ' + str([x.id for x in self.neighbours])