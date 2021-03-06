import random
import math
from queue import LifoQueue
from nQueens import State

cutoff  = State('cutoff', None, math.inf)


#implementation of depth limited portion of id
def depth_limited(problem, depth):
    queue = LifoQueue()
    initial = problem.initial1()
    queue.put(initial)
    
    while True:
        #print(depth, queue.qsize())
        if queue.empty():
            return None
        current = queue.get()
        if problem.goal_test(current.state) == True:
            return current
        elif current.depth is not depth:
            for successor in problem.children1(current):
                queue.put(successor)


def iterative_deepening_search(problem):
    limit = 20
    depth = 0
    result = None
    while result == None:
        if depth >= limit:
            result = cutoff
        else:
            result = depth_limited(problem, depth)
        depth +=1
    return result.state