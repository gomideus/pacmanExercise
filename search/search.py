# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start estadoAtual for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, estadoAtual):
        """
          estadoAtual: Search estadoAtual

        Returns True if and only if the estadoAtual is a valid goal estadoAtual.
        """
        util.raiseNotDefined()

    def getSuccessors(self, estadoAtual):
        """
          estadoAtual: Search estadoAtual

        For a given estadoAtual, this should return a list of triples, (sucessor,
        movimento, stepCost), where 'sucessor' is a sucessor to the current
        estadoAtual, 'movimento' is the movimento required to get there, and 'stepCost' is
        the incremental cost of expanding to that sucessor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, movimento):
        """
         movimento: A list of movimento to take

        This method returns the total cost of a particular sequence of movimento.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]    
    
def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of movimento that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    from util import Stack
    from game import Directions
    
    start = problem.getStartState()
    sucCoord = start
    visitado = []
    visitado.append(start) # Seta pos inicial como visitada
    fronteira = Stack() # Declaracao da pilha
    tupla = (start, [])
    fronteira.push(tupla)

    while not fronteira.isEmpty() and not problem.isGoalState(sucCoord):

        estadoAtual, movimento = fronteira.pop()
        visitado.append(estadoAtual) # Seta elemento atual como visitado
        sucessor = problem.getSuccessors(estadoAtual)
        
        for i in sucessor:
            if not i[0] in visitado:
                sucCoord = i[0]
                direction = i[1]
                fronteira.push((i[0], movimento + [direction]))

    return movimento + [direction]
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    visitado = []
    visitado.append(start)
    fronteira = util.Queue()
    tupla = (start, [])
    fronteira.push(tupla)
    while not fronteira.isEmpty():
        estadoAtual, movimento = fronteira.pop()
        if problem.isGoalState(estadoAtual):
            return movimento
        sucessor = problem.getSuccessors(estadoAtual)
        for i in sucessor:
            if not i[0] in visitado:
                direction = i[1]
                visitado.append(i[0])
                fronteira.push((i[0], movimento + [direction]))
    return movimento
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    visitado = []
    fronteira = util.PriorityQueue()
    fronteira.push((start, []) ,0)
    while not fronteira.isEmpty():
        estadoAtual, actions = fronteira.pop()
        if problem.isGoalState(estadoAtual):
            return actions
        if estadoAtual not in visitado:
            successors = problem.getSuccessors(estadoAtual)
            for succ in successors:
                if succ[0] not in visitado:
                    directions = succ[1]
                    newCost = actions + [directions]
                    fronteira.push((succ[0], actions + [directions]), problem.getCostOfActions(newCost))
        visitado.append(estadoAtual)
    return actions
    
    util.raiseNotDefined()

def nullHeuristic(estadoAtual, problem=None):
    """
    A heuristic function estimates the cost from the current estadoAtual to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    visitado = []
    fronteira = util.PriorityQueue()
    fronteira.push((start, []), nullHeuristic(start, problem))
    nCost = 0
    while not fronteira.isEmpty():
        estadoAtual, actions = fronteira.pop()
        if problem.isGoalState(estadoAtual):
            return actions
        if estadoAtual not in visitado:
            successors = problem.getSuccessors(estadoAtual)
            for succ in successors:
                if succ[0] not in visitado:
                    directions = succ[1]
                    nActions = actions + [directions]
                    nCost = problem.getCostOfActions(nActions) + heuristic(succ[0], problem)
                    fronteira.push((succ[0], actions + [directions]), nCost)
        visitado.append(estadoAtual)
    return actions
    util.raiseNotDefined()
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
