import math
import pandas as pd
import matplotlib.pyplot as plt

class MyFDT:
    def __init__(self, arrData) -> None:
        self.data           = arrData
        self.data           = sorted(self.data);
        self.dataSize       = len(arrData)
        self.lowest         = self.data[0]
        self.highest        = self.data[self.dataSize-1];
        self.classSize      = math.ceil((self.highest - self.lowest)/((1+3.322)*math.log10(self.dataSize)));
        self.classWidth     = int(self.classSize - 1); # Interval
        
        # Set-up the interval
        self.classIntervalL   = []
        self.classIntervalH   = []
        self.classIntervalStr = []
        self.__setUpInterval()

        # Calculate the Class Frequency
        self.classFrequency = []
        self.__calcFrequency()

        # Calculate X value
        self.xValue = []
        self.__calcX()

        self.classBoundaryL = []
        self.classBoundaryH = []
        self.classBoundaryStr = []
        self.__calcCb()
        
        
        self.lCf = []
        self.gCf = []
        self.__calcCf()

        self.rf = []
        self.__calcRf()

        print("Highest Value: " + str(self.highest))
        print("Lowest value: " + str(self.lowest))

        df = pd.DataFrame(columns=['Class Interval', 'f', 'x', 'cb', '<cf', '>cf', 'rf'])
        for i in range(0, self.classWidth):  
            df.loc[i] = [self.classIntervalStr[i], self.classFrequency[i],
                           self.xValue[i], self.classBoundaryStr[i], self.lCf[i],
                           self.gCf[i], self.rf[i]]
        
        print(df.head(10))
        

    def plotOGive(self):
        fig, axs = plt.subplots()
        axs.plot(self.classIntervalH, self.lCf)
        axs.plot(self.classIntervalH, self.gCf)
        plt.show()
    
    def plotBoxChart(self):
        fig, axs = plt.subplots()
        axs.bar(self.xValue, self.classFrequency, width=10, edgecolor="white", linewidth=0.7)
        plt.show()
    
    def plotPoly(self):
        fig,axs = plt.subplots()
        tempXValue = []
        tempXValue += self.xValue


        tempFValue = []
        tempFValue += self.classFrequency

        axs.plot(tempXValue, tempFValue)
        plt.show()
    
    def __setUpInterval(self):
        lValue = self.lowest
        hValue = self.lowest+self.classWidth
        for i in range(0, int(self.classSize)):
            self.classIntervalL.append(lValue)            
            self.classIntervalH.append(hValue)            
            self.classIntervalStr.append(str(lValue) + "-" + str(hValue))
            lValue = hValue+1
            hValue = lValue+self.classWidth

    def __calcFrequency(self):
        intervalIndex = 0
        count = 0
        for i in self.data:
            if i <= self.classIntervalH[intervalIndex]:
                count += 1
            else:
                self.classFrequency.append(count)
                count = 1
                intervalIndex += 1
        self.classFrequency.append(count)
        count = 1
        intervalIndex += 1
        while intervalIndex < self.classSize:
            self.classFrequency.append(0)
            intervalIndex += 1

    def __calcX(self):
        for i in range(0, self.classSize):
            self.xValue.append((self.classIntervalL[i] + self.classIntervalH[i])//(2))
            
    def __calcCb(self):
        for i in range(0, self.classSize):
            self.classBoundaryL.append(self.classIntervalL[i] - 0.5)
            self.classBoundaryH.append(self.classIntervalH[i] + 0.5)
            self.classBoundaryStr.append(str(self.classBoundaryL[i]) + "-" + str(self.classBoundaryH[i]))
        pass
    
    def __calcCf(self):
        summation = 0
        for i in range(0, self.classSize):
            summation += self.classFrequency[i]
            self.lCf.append(summation)
        summation = 0
        for i in range(0, self.classSize):
            summation += self.classFrequency[self.classSize-1-i]
            self.gCf.append(summation)
        self.gCf.reverse()

    def __calcRf(self):
        for i in self.classFrequency:
            self.rf.append((i/self.dataSize)*100)
    
    pass

water = MyFDT([
        18,29,42,57,61,67,37,49,53,47,
        24,34,45,58,63,70,39,51,54,48,
        28,36,46,60,66,77,40,52,56,49,
        19,31,44,58,62,68,38,50,54,58,
        27,36,46,59,64,74,39,51,55,48
])

water.plotPoly()