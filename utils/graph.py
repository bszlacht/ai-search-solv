from utils.vertex import Vertex

#TODO: Typowanie
#TODO: Uogólnić tą klasę jak się da i są pomysły

"""
Rozwiązanie testowe. Do zmiany.
Można zrobić zwykłą klasę grafu. Później grafu z wagami oraz grafu na gridzie. Będą po sobie dziedziczyły.
"""

class Graph():
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0
    
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self, id):
        if id in self.vertexList:
            return self.vertexList[id]
        else:
            return None

    def addEgde(self, f, t, weight=0):
        if f not in self.vertexList:
            nv = self.addVertex(f)
        if t not in self.vertexList:
            nv = self.addVertex(t)
        self.vertexList[f].addNeighbour(self.vertexList[t], weight)
    
    def getVertices(self):
        return self.vertexList.keys()

    def __contains__(self, id):
        return id in self.vertexList

    def __iter__(self):
        return iter(self.vertexList.values())