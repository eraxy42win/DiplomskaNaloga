import sys
sys.path.append('../')
import numpy as np
from NiaPy.algorithms.basic import FireflyAlgorithm
from NiaPy.task.task import StoppingTask, OptimizationType
 
class Runner(object):
    
    def RunAlgorithm(self, NUM_RUNS,D,Np,nFES,BenchFunction):
        rawData = np.zeros(NUM_RUNS)
        for i in range(NUM_RUNS):
            task = StoppingTask(D=D, nFES=nFES, optType=OptimizationType.MINIMIZATION, benchmark=BenchFunction)
            algo = FireflyAlgorithm(NP=Np, alpha=0.5, betamin=0.2, gamma=1.0)
            best = algo.run(task=task)
            rawData[i] = best[1]
            print(rawData[i])
        return rawData