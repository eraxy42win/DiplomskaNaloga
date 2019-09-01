import pandas as pd

class Storage(object):

    #Vrnemo dataframe
    def SaveDataToDataframe(self,data,elapsedTime,BenchFunctionName):
      resultArray = []
      resultArray.append(data.min_value())
      resultArray.append(data.max_value())
      resultArray.append(data.mean())
      resultArray.append(data.median())
      resultArray.append(data.standard_deviation())
      resultArray.append(elapsedTime)
      DFresult = pd.DataFrame(data=[resultArray], index=[BenchFunctionName], columns=['Min', 'Max','Mean','Median','Standard_D','Time'])
      return DFresult
        
