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
         movimento: A list of moves to take

        This method returns the total cost of a particular sequence of moves.
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

    from util import Queue

    fila = Queue()
    atual = problem.getStartState()
    tupla = (atual, [])
    fila.push(tupla)
    visited = []

    while not problem.isGoalState(atual):

        atual, movimentos = fila.pop()
        succ = problem.getSuccessors(atual) # (sucessor, movimento, stepCost)
        visited.append(atual)
        for i in succ:
            if not i[0] in visited:
                move = i[1]
                fila.push((i[0], movimentos + [move]))

    return movimentos
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    fila = []
    atual = problem.getStartState()
    tupla = ([atual], 0, [])
    fila.append(tupla)
    visited = []

    while not problem.isGoalState(atual) and fila:
        nodes, cost, moves = fila.pop(0)
        atual = nodes[-1]
        succ = problem.getSuccessors(atual) # (sucessor, movimento, stepCost)
        visited.append(atual)
        for i in succ:
            if not i[0] in visited:
                move = i[1]
                fila.append((nodes+[i[0]], cost+i[2], moves + [move]))
        fila = sorted(fila, key=lambda tup: tup[1])
    return moves

    
    util.raiseNotDefined()

def nullHeuristic(estadoAtual, problem=None):
    """
    A heuristic function estimates the cost from the current estadoAtual to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def manhattanHeuristic(estadoAtual, problem=None):
    return abs( 1 - estadoAtual[0] ) + abs( 1 - estadoAtual[1] )

def euclideanHeuristic(estadoAtual, problem=None):
    # dAB² = (xB – xA)² + (yB – yA)².
    import math
    return math.sqrt( ( (estadoAtual[0] - 1 )**2) + ( (estadoAtual[1] - 1 )**2) )

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    fila = []
    atual = problem.getStartState()
    tupla = ([atual], 0, [])
    fila.append(tupla)
    visited = []

    while not problem.isGoalState(atual) and fila:
        nodes, cost, moves = fila.pop(0)
        atual = nodes[-1]
        succ = problem.getSuccessors(atual) # (sucessor, movimento, stepCost)
        visited.append(atual)
        for i in succ:
            if not i[0] in visited:
                move = i[1]
                custoTotal = cost + i[2] + heuristic(i[0],problem)
                fila.append((nodes+[i[0]], custoTotal, moves + [move]))
        fila = sorted(fila, key=lambda tup: tup[1])
    return moves

    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
