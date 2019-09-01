import sys
sys.path.append('../')
import pandas as pd
import time
import numpy as np
import runner
import Procesing
import Storage
 
from NiaPy.benchmarks import Ackley,Rastrigin,Rosenbrock,Griewank,Sphere,Whitley,Zakharov,Perm,Powell,Pinter

#input parameters
ArrayOfNP = [10,20]#,30,50,75,100
ArrayOfBenchmarks = [Ackley(),Rastrigin()]#,Rosenbrock(),Griewank(), Sphere(), Whitley(), Zakharov(), Perm(), Powell(), Pinter()
ArrayOfnFES = [10000]#,20000,30000
ArrayOfD = [10]#,20,30
NUM_RUNS = 1

resultFilePath = 'results.xlsx' 
Processor = Procesing.Procesing()
Runner = runner.Runner()
Storage = Storage.Storage()

beginningTime = time.time()
with pd.ExcelWriter('results.xlsx') as writer:
    for Np in ArrayOfNP:
        for nFES in ArrayOfnFES:
            for D in ArrayOfD:
                tempDataFrame = []
                for BenchFunction in ArrayOfBenchmarks:
					#start the timer
                    start = time.time()
					#Execute the Firefly Algorithm
                    rawData = Runner.RunAlgorithm(NUM_RUNS,D,Np,nFES,BenchFunction)
                    end = time.time()

                    elapsedTime = end - start
					#Get the statistics results
                    Data = Processor.ProcesData(rawData)
                    df = Storage.SaveDataToDataframe(Data,elapsedTime,BenchFunction.Name)
                    tempDataFrame.append(df)
                result = pd.concat(tempDataFrame)
                name = 'NP_' + str(Np) + ' - nFES_' + str(nFES) + ' - D_' + str(D)
                result.to_excel(writer,sheet_name=name)

endTime = time.time()
elapsedTimeOffAllRuns = endTime - beginningTime
print(elapsedTimeOffAllRuns)