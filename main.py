from IterativeDeepeningSearch import iterative_deepening_search
from HillClimbing import hill_climbing, random_restart
from SimulatedAnnealing import simulated_annealing
from nQueens import NQueensSearch

from time import time

TEST_TIMES = 1

class TestSearch(object):
    def printBoard(self, result):
        n = len(result)
        
        for i in range(0,n):
            row = '|'
            for j in range(0,n):
                if result[i] == j:
                    row += '#|'
                else:
                    row += ' |'
            print(row)

    def testSearch(self, problem, search):
        times = TEST_TIMES
        cnt = 0
        start = time()
        for i in range(times):
            result = search(problem)
            if problem.value(result) == 0:
                cnt += 1
            #self.printBoard(result)
        print(" - Accuracy: %2d/%d\tRunning time: %f seconds"%(cnt, times, time()-start))


if __name__ == "__main__":
    test = TestSearch()

    print("Running search for N Queens Problem")
    size = eval(input(" - Please input the size of the board: "))
    print()

    algorithms = [
        iterative_deepening_search,
        hill_climbing,
        random_restart,
        simulated_annealing
    ]

    names = [
        "Iterative Deepening Search",
        "Hill Climbing",
        "Random Restart Hill Climbing",
        "Simulated Annealing"
    ]

    problem = NQueensSearch(size)
 
   
    for i in range(len(algorithms)):
        print(names[i])
        board = test.testSearch(problem, algorithms[i])
        
        