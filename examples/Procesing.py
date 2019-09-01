import sys
sys.path.append('../')
from NiaPy.algorithms.statistics import BasicStatistics
  
class Procesing(object):
    
    #Nad podatki klicemo operacije statistike (Min,Max,Mean,Median,Standardni odklon)
    def ProcesData(self,rawData):
        processedData = BasicStatistics(rawData)
        return processedData


