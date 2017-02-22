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
from test.pyclbr_input import Other


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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    e = Directions.EAST
    n = Directions.NORTH
    w = Directions.WEST
    
    fringe = util.Stack()
    returnlist = []
    closed = []
    
    currentState = problem.getStartState()
    currentNode = [currentState, []]
    fringe.push(currentNode)
    
    if problem.isGoalState(currentState):
        return []
    
    path_found = False
    
    while (path_found != True):
        popped = fringe.pop()
#         print "Search: popped x, y: %r, %r" % (popped.getState().getLocation())
        if (popped[0] in closed):
            continue
        else:
            closed.append(popped[0])
            if problem.isGoalState(popped[0]):
                path_found = True
                returnlist = popped[1]
                return returnlist
            else:
                for possible in problem.getSuccessors(popped[0]):
                    newstate = possible[0]
    #                 print "Search: successor: %r" % (str(possible[1]))
                    if newstate in closed:
    #                     print "Search: newstate %r, %r already in closed" % (possible[0].getLocation())
                        continue;
                    else:
                        newPath = popped[1][:]
                        newPath.append(possible[1])
                        newNode = [newstate, newPath]
    #                     print "Search: sending %r to fringe" % str((possible[1]))
                        fringe.push(newNode)
    #                     print "Fringe size: %r" % fringe.list.__len__()
    return returnlist

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    e = Directions.EAST
    n = Directions.NORTH
    w = Directions.WEST

    fringe = util.Queue()
    returnlist = []
    closed = []
    
    currentState = problem.getStartState()
    currentNode = [currentState, []]
    fringe.push(currentNode)
    
    if problem.isGoalState(currentState):
        return []
    
    path_found = False
    
    while (path_found != True):
        popped = fringe.pop()
#         popstate = popped[0][:]
#         print "Search: popped x, y: %r, %r" % (popped.getState().getLocation())
        if (popped[0] in closed):
            continue
        else:
            closed.append(popped[0])
            if problem.isGoalState(popped[0]):
                path_found = True
                returnlist = popped[1]
                return returnlist
            else:
                for possible in problem.getSuccessors(popped[0]):
                    newstate = possible[0]
    #                 print "Search: successor: %r" % (str(possible[1]))
                    if newstate in closed:
    #                     print "Search: newstate %r, %r already in closed" % (possible[0].getLocation())
                        continue;
                    else:
                        newPath = popped[1][:]
                        newPath.append(possible[1])
                        newNode = [newstate, newPath]
    #                     print "Search: sending %r to fringe" % str((possible[1]))
                        fringe.push(newNode)
    #                     print "Fringe size: %r" % fringe.list.__len__()
    return returnlist

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return aStarSearch(problem)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    e = Directions.EAST
    n = Directions.NORTH
    w = Directions.WEST
    
    fringe = util.PriorityQueue()
    returnlist = []
    closed = []
    
    currentState = problem.getStartState()
    currentNode = [currentState, [], 0]
    fringe.push(currentNode, 0)
    
    if problem.isGoalState(currentState):
        return []
    
    path_found = False
    
    while (path_found != True):
        popped = fringe.pop()
#         print "Search: popped x, y: %r, %r" % (popped.getState().getLocation())
        if (popped[0] in closed):
            continue
        else:
            closed.append(popped[0])
            if problem.isGoalState(popped[0]):
                path_found = True
                returnlist = popped[1]
                return returnlist
            else:
                for possible in problem.getSuccessors(popped[0]):
                    newstate = possible[0]
    #                 print "Search: successor: %r" % (str(possible[1]))
                    if newstate in closed:
    #                     print "Search: newstate %r, %r already in closed" % (possible[0].getLocation())
                        continue;
                    else:
                        newPath = popped[1][:]
                        newPath.append(possible[1])
                        heuristicVal = heuristic(newstate, problem)
                        newNode = [newstate, newPath, possible[2]+popped[2]]
    #                     print "Search: sending %r to fringe" % str((possible[1]))
                        fringe.push(newNode, heuristicVal+popped[2]+possible[2])
    #                     print "Fringe size: %r" % fringe.list.__len__()
    return returnlist

    util.raiseNotDefined()

# 
# class CostNode:
#     def __init__(self, parent, state, move, incrementCost, cost):
#         self.parent = parent
#         self.state = state
#         self.move = move
#         self.incrementCost = incrementCost
#         self.cost = cost
#     
#     def getParent(self):
#         return self.parent
#     
#     def getState(self):
#         return self.state
#     
#     def getMove(self):
#         return self.move
#     
#     def getCost(self):
#         return self.cost
#     
#     def setCost(self, newcost):
#         self.cost = newcost
#     
#     def getincrementCost(self):
#         return self.incrementCost
#     
# 
# class Node:
#     def __init__(self, parent, state, move, incrementCost):
#         self.parent = parent
#         self.state = state
#         self.move = move
#         self.incrementCost = incrementCost
#     
#     def getParent(self):
#         return self.parent
#     
#     def getState(self):
#         return self.state
#     
#     def getMove(self):
#         return self.move
# 
#     def getincrementCost(self):
#         return self.incrementCost
#     

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
