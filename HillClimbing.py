import random
from sre_parse import State

# Hill Climbing in continuous space is Gradient Descent
def hill_climbing(problem):
    # Keep choosing the neighbour with highest value until no neighbor is better
    current = problem.initial()
    while True:
        neighbours = problem.children(current)
        if not neighbours:
            break
        neighbour = max(neighbours,
                key=lambda state: (problem.value(state.state), random.random()))
        if problem.value(neighbour.state) <= problem.value(current.state):
            break
        current = neighbour
    return current.state

def random_restart(problem, limit = 10):
    state = problem.initial().state
    cnt = 0
    while problem.goal_test(state) == False and cnt < limit:
        state = hill_climbing(problem)
        cnt += 1
    return state