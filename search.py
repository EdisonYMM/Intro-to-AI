# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    Visited_list = []
    Direction_list = []
    State_list = util.Stack()
    if not problem.isGoalState(problem.getStartState()):
        State_list.push((problem.getStartState(),Direction_list,0))
        Visited_list.append(problem.getStartState())
    while not State_list.isEmpty():
        temp,direction,cost = State_list.pop()
        if problem.isGoalState(temp):
            return direction
        Visited_list.append(temp)
        for newState,newDirection,newCost in problem.getSuccessors(temp):
            if newState not in Visited_list:
                newpath = direction + [newDirection]
                State_list.push((newState,newpath,newCost))                 
    
    util.raiseNotDefined()
    
def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    Visited_list = []
    Direction_list = []
    State_list = util.Queue()
    State_list.push((problem.getStartState(),Direction_list,0))
    while not State_list.isEmpty():
        temp,direction,cost = State_list.pop()
        if temp not in Visited_list:
            if problem.isGoalState(temp):
                return direction
            else:
                for newState,newDirection,newCost in problem.getSuccessors(temp):
                    newpath = direction + [newDirection]
                    State_list.push((newState,newpath,newCost))
                Visited_list.append(temp)
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    Visited_list = []
    Direction_list = []
    State_list = util.PriorityQueue()
    State_list.push((problem.getStartState(),Direction_list,0),0)
    while not State_list.isEmpty():
        currentNode = State_list.pop()
        currentState = currentNode[0]
        currentDirection = currentNode[1]
        currentCost = currentNode[2]
        if currentState not in Visited_list:
                if problem.isGoalState(currentState):
                    return currentDirection
                else:
                    for newNode in problem.getSuccessors(currentState):
                        newState = newNode[0]
                        newPath = currentDirection + [newNode[1]]
                        newCost = currentCost + newNode[2]
                        State_list.push((newState,newPath,newCost),newCost)
                    Visited_list.append(currentState)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    Visited_list = []
    Direction_list = []
    State_list = util.PriorityQueue()
    State_list.push((problem.getStartState(),Direction_list,0),0)
    while not State_list.isEmpty():
        currentNode = State_list.pop()
        currentState = currentNode[0]
        currentDirection = currentNode[1]
        currentCost = currentNode[2]
        if currentState not in Visited_list:
                if problem.isGoalState(currentState):
                    return currentDirection
                else:
                    for newNode in problem.getSuccessors(currentState):
                        newState = newNode[0]
                        newPath = currentDirection + [newNode[1]]
                        newCost = currentCost + newNode[2]
                        totalCost = currentCost + newNode[2] + heuristic(newState,problem)
                        State_list.push((newState,newPath,newCost),totalCost)
                    Visited_list.append(currentState)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
