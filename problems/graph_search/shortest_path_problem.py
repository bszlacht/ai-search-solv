from utils import Graph

#TODO: Zdefiniować problem
#TODO: Typowanie

class ShortestPathProblem():
    def __init__(self):
        self.graph = Graph()
        self.start_config = {}
        self.goal_config = {}

    def __str__(self) -> str:
        return "SPP: From\n" + str(self.start_config) + "\nTo:\n" + str(self.goal_config)

    """ 
    Chcemy mieć początkowy `stan` od razu? Czy najpierw startową konfigurację, która przejdzie w stan?
    Nazewnictwo: startState lub startConfig (?)
    """
    
    def startState(self):
        self.start_config = {'start': 1}
        return self.start_config
        
    def goalState(self):
        self.goal_config = {'goal': 0}
        return self.goal_config