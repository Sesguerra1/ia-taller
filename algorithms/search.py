from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    
    
    estructura = utils.Stack()
    estructura.push((start,[]))
    explorados = set()
    
    while not estructura.isEmpty():
        state, actions = estrucutura.pop()
        if state in explorados:
            continue 
        
        explorados.add(state)
        
        if problem.isGoalState(state):
            return actions 
        
        for succ , action , _stepCost in problem.getSuccessors(state):
            if succ not in explorados:
                estructura.push((succ , actions + [action])) 
        
    return []
        
    
    utils.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    estructura = utils.Queue()
    explorados = set()
    estructura.push((start,[]))
    explorados.add(start)
    while not estructura.isEmpty():
        state, actions = estructura.pop()
        if problem.isGoalState(state):
            return actions 
        for succ , action , _stepCost in problem.getSuccessors(state):
            if succ not in explorados:
                explorados.add(succ)
                estructura.push((succ , actions + [action]))
    return []
    utils.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    
    estructura = utils.PriorityQueue()
    estructura.push((start,[],0)0)
    mejor = {start : 0}
    
    while not estructura.isEmpty ():
        state , actions , mej = estructura.pop()
        
        if mej != mejor.get(state, float("inf")):
            continue
            
        if problem.isGoalState(state):
            return actions 
        
        for succ, action, stepCost in problem.getSuccessors(state):
            nuevo_mej = mej + stepCost
            if nuevo_mej < mejor.get(succ, float("inf")):
                mejor[succ] = nuevo_mej
                frontier.push((succ, actions + [action], nuevo_mej), nuevo_mej)

    return []
        
    utils.raiseNotDefined()


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []
    estructura = utils.PriorityQueue()
    estructura.push((start,[],0),heuristic(start, problem))
    mejor = {start : 0}
    while not estructura.isEmpty ():
        state,actions, mej = estructura.pop()
        if mej != mejor.get(state, float("inf")):
            continue
        if problem.isGoalState(state):
            return actions
        for succ, action, stepCost in problem.getSuccessors(state):
            nuevo_mej = mej + stepCost
            if nuevo_mej < mejor.get(succ, float("inf")):
                mejor[succ] = nuevo_mej
                mejor_con_heuristica = nuevo_mej + heuristic(succ, problem)
                estructura.push((succ, actions + [action], nuevo_mej), mejor_con_heuristica)
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
