from random import choice
from collections import defaultdict
from collections import Counter
from random import randrange

class State:
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth


class SearchProblem:
    def __init__(self, initial=None):
        """Initialize a search problem with a initial state"""
        pass
    
    def initial1(self):
        """Return default initial state of the search problem"""
        pass

    def initial2(self):
        """Return default initial state of the search problem"""
        pass

    def goal_test(self, state):
        """Return True if the state is a goal"""
        pass

    def value(self, state):
        """For optimization problems, each state has a value to be maximized"""
        pass

    def children2(self, state):
        """Return children of the given state"""
        pass

    def random_child(self, state):
        """Return a random child of the state, used in simulated annealing"""
        return choice(self.children2(state))


class NQueensSearch(SearchProblem):

    def __init__(self, N):
        self.N = N

    def initial1(self):
        return  State(tuple([None] * self.N), None, 0)

    def initial2(self):
        return  State(tuple(randrange(self.N) for i in range(self.N)), None, 0)

    def goal_test(self, state):
        if not self.all_queens_placed(state):
            return False
        return not any(self.clashes(state, state[col], col)
                for col in range(len(state)))

    def value(self, state):
        """ -Number of pairs of queens attacking each other """
        shu, pie, na = [Counter() for i in range(3)]
        for row, col in enumerate(state):
            shu[col] += 1
            pie[row - col] += 1
            na[row + col] += 1
        clashes = 0
        for cnt in [shu, pie, na]:
            for key in cnt:
                clashes += cnt[key] * (cnt[key] - 1) // 2
        return -clashes

    def children1(self, node):
        return [ State(self.place_queen(node, move), node, node.depth + 1) for move in self.get_moves(node) ]

    def get_moves(self, node):
        #check if all queens have been placed
        if not self.all_queens_placed(node.state):
            col = self.get_empty_column(node.state)
            return [ row for row in range(self.N) if not self.clashes(node.state, row, col) ] 
        return list()
            
    def get_empty_column(self, state):
        return state.index(None)
    
    def all_queens_placed(self, state):
        return state[-1] != None

    def clashes(self, state, row, column):
        return any(self.clash(row, column, state[idx], idx) for idx in range(column))

    def clash(self, row_1, column_1, row_2, column_2):
        return (row_1 == row_2 or
                column_1 == column_2 or  
                row_1 - column_1 == row_2 - column_2 or  
                row_1 + column_1 == row_2 + column_2)
    
    def place_queen(self, node, queen):
        column = self.get_empty_column(node.state)
        new_state = list(node.state)
        new_state[column] = queen
        return tuple(new_state)

    def children2(self, state):
        children = []
        for row in range(self.N):
            for col in range(self.N):
                if col != state.state[row]:
                    child = list(state.state)
                    child[row] = col
                    children.append(State(tuple(child), state, state.depth+1))
        return children

    def random_child(self, state):
        row = randrange(self.N)
        col = randrange(self.N - 1)
        if col >= state[row]:
            col += 1
        child = list(state)
        child[row] = col
        return tuple(child)