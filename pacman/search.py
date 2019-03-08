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


#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
num_hours_i_spent_on_this_assignment = 0
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>

"""
#####################################################
#####################################################



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


def dfs_search(problem):
    discovered = []
    s = util.Stack()
    s.push((problem.getStartState(), []))
    while not s.isEmpty():
        pos, actionList = s.pop()
        if problem.isGoalState(pos):
            return actionList
        if not pos in discovered:            
            discovered.append(pos)
            #print("discovered:", pos, " - move:", actionList)
            for successor, action, stepCost in problem.getSuccessors(pos):
                # print("\t", successor, action, stepCost)
                # We need to keep all the actions needed for each node
                # so we add the each successor action to the actionList
                s.push((successor, actionList + [action]))


#Coded for Question 2.1
def bfs_search_new(problem):
    mainActionList = []
    while len(problem.cornersLeft) > 0:
        discovered = []
        q = util.Queue()
        q.push((problem.getStartState(), []))
        while not q.isEmpty():
            pos, actionList = q.pop()
            if problem.isGoalState(pos):
                mainActionList.extend(actionList)
                break
            if not pos in discovered:            
                discovered.append(pos)
                #print("discovered:", pos, " - move:", actionList)
                for successor, action, stepCost in problem.getSuccessors(pos):
                    # print("\t", successor, action, stepCost)
                    # We need to keep all the actions needed for each node
                    # so we add the each successor action to the actionList
                    q.push((successor, actionList + [action]))
    return mainActionList


def bfs_search(problem):
    discovered = []
    q = util.Queue()
    q.push((problem.getStartState(), []))
    while not q.isEmpty():
        pos, actionList = q.pop()
        if problem.isGoalState(pos):
            return actionList
        if not pos in discovered:            
            discovered.append(pos)
            #print("discovered:", pos, " - move:", actionList)
            for successor, action, stepCost in problem.getSuccessors(pos):
                # print("\t", successor, action, stepCost)
                # We need to keep all the actions needed for each node
                # so we add the each successor action to the actionList
                q.push((successor, actionList + [action]))
    

def depthFirstSearch(problem):
    """
    Questoin 1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    print (problem.isGoalState(problem.getStartState()) )
    print ( problem.getSuccessors(problem.getStartState()) )

    python pacman.py -l tinyMaze -p SearchAgent
    python pacman.py -l mediumMaze -p SearchAgent
    python pacman.py -l bigMaze -z .5 -p SearchAgent

    """
    "*** YOUR CODE HERE ***"
    coordinates = util.Queue()
    visitedCoordinates = [] 
    coordinates.push((problem.getStartState(),[], 0)) #Starting point is not a tuple, so we make it one before pushing it
    while not coordinates.isEmpty():
        currentPosition, lastMoves, totalCost = coordinates.pop()
        if problem.isGoalState(currentPosition): return lastMoves
        elif currentPosition not in visitedCoordinates:
            visitedCoordinates.append(currentPosition)
            for nextPosition, nextAction, nextCost in problem.getSuccessors(currentPosition):
                coordinates.push((nextPosition, lastMoves + [nextAction], nextCost+totalCost))

    # print ( problem.getStartState() )
    # print ( problem.isGoalState(problem.getStartState()) )
    # print ( problem.isGoalState((4,5)) )
   
    # actions = dfs_search(problem)
    # # print()
    # # print('Yoo-Hoo ====>>>>', actions)
    # # print()
    # return actions


def breadthFirstSearch(problem):
    """Questoin 1.2
     Search the shallowest nodes in the search tree first.

     python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
     python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
     """
     
    "*** YOUR CODE HERE ***"
    actions = bfs_search(problem)
    # print()
    # print('Yoo-Hoo ====>>>>', actions)
    # print()
    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return util.manhattanDistance(state, problem.goal)

# This is done using python Queue
from queue import PriorityQueue
def aStarSearchP(problem, heuristic=nullHeuristic):
    """Question 1.3    
        python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astarp,heuristic=manhattanHeuristic
        python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astarp,heuristic=manhattanHeuristic
    Search the node that has the lowest combined cost and heuristic first."""    
    "*** YOUR CODE HERE ***"
    discovered = []
    pq = PriorityQueue()
    pq.put((heuristic(problem.getStartState(), problem), problem.getStartState(), []))
    while not pq.empty():
        cost, pos, actionList = pq.get()
        # print(cost)
        if problem.isGoalState(pos):            
            return actionList
        if not pos in discovered:            
            discovered.append(pos)
            #print("discovered:", pos, " - move:", actionList)
            for successor, action, stepCost in problem.getSuccessors(pos):
                # print("\t", successor, action, stepCost)
                # We need to keep all the actions needed for each node
                # so we add the each successor action to the actionList
                cost = heuristic(pos, problem) + len(actionList + [action])
                pq.put((cost, successor, actionList + [action]))


# this is done using util.Queue
def aStarSearch(problem, heuristic=nullHeuristic):
    """Question 1.3
    
    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

    Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    discovered = []
    pq = util.PriorityQueue()    
    pq.push((problem.getStartState(), []), heuristic(problem.getStartState(), problem))
    while not pq.isEmpty():
        pos, actionList = pq.pop()        
        if problem.isGoalState(pos):            
            return actionList
        if not pos in discovered:            
            discovered.append(pos)
            #print("discovered:", pos, " - move:", actionList)
            for successor, action, stepCost in problem.getSuccessors(pos):
                # print("\t", successor, action, stepCost)
                # We need to keep all the actions needed for each node
                # so we add the each successor action to the actionList
                cost = heuristic(pos, problem) + len(actionList + [action])
                pq.push((successor, actionList + [action]), cost)




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch   # with util Queue
astarp = aStarSearchP  # with python Queue
