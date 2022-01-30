from IterativeDeepeningSearch import iterative_deepening_search
from HillClimbing import hill_climbing, random_restart
from SimulatedAnnealing import simulated_annealing
from nQueens import NQueensSearch

from time import time

import pandas as pd
import numpy as np

TEST_TIMES = 10
MODE = 0 # 1
SIZES = range(4, 31)

ALGORITHMS = {
            "IDS": iterative_deepening_search,
            "HC": hill_climbing,
            "RRHC": random_restart,
            "SA": simulated_annealing
    }
NAMES = {
            "IDS": "Iterative Deepening Search",
            "HC": "Hill Climbing",
            "RRHC": "Random Restart Hill Climbing",
            "SA": "Simulated Annealing"
    }
TIMESDATA = {
            "size": SIZES,
            "IDS": [],
            "HC": [],
            "RRHC": [],
            "SA": []
        }

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
            if problem.goal_test(result) == True:
                cnt += 1
            #self.printBoard(result)
        print(" - Accuracy: %2d/%d\tRunning time: %f seconds"%(cnt, times, time()-start))
    

    def testMultipleResults(self, algorithms, names):
        sizes = SIZES
        timesData = TIMESDATA
        for key in algorithms:
            print(names[key])
            timesMed = []
            for size in sizes:
                if key == 'IDS' and size > 12:
                    break
                cnt = 0
                problem = NQueensSearch(size)
                times = []
                for i in range(TEST_TIMES):
                    start = time()
                    result = algorithms[key](problem)
                    times.append(time()-start)
                    if problem.goal_test(result) == True:
                        cnt += 1
                timesMed.append(np.mean(times))
                print(f" - Size: {size}\t Accuracy: {cnt}/{TEST_TIMES}\t Mean Running Time: {round(timesMed[-1], 5)} seconds")
            timesData[key] = timesMed
        
        data = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in timesData.items()]))
        data.to_csv('times5.csv', index = False)

            
            
if __name__ == "__main__":
    test = TestSearch()
    algorithms = ALGORITHMS
    names = NAMES


    if MODE == 0:
        test.testMultipleResults(algorithms, names)


    if MODE == 1:
        print("Running search for N Queens Problem")
        size = eval(input(" - Please input the size of the board: "))
        print()

        problem = NQueensSearch(size)
    
        for key in algorithms:
            print(names[key])
            board = test.testSearch(problem, algorithms[key])
        
        