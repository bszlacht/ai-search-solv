from solvers import *
from problems.graph_search.shortest_path_problem import ShortestPathProblem
from utils.state import State

if __name__ == '__main__':
    # Define solution object
    s = Solver()
    # Define problem object
    p = ShortestPathProblem()

    # Start config
    start = p.startState()

    # Root state
    root_state = State(start)
    # Goal state
    goal = p.goalState()

    print(p)
    print(root_state)
