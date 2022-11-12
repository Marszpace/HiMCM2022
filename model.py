import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numdifftools as nd

def static(Xn,k,rmax):
    return rmax*(k-Xn)/k*Xn+Xn

def seasonal(Xn,time,data,coefficient):
    res=0
    for i in range(len(data)):
        res+=data[i]*coefficient[i]
    return res

class model:
    def load_data(self):
        #data=["example.csv","example2.csv"]
        #main="data.csv"
        data=[]

        #load actual data
        df=pd.read_csv(i)
        self.actual=df.values.tolist()
        
        #load parameter data
        n=0
        for i in data:
            df=pd.read_csv(i)
            self.data.append(df.values.tolist())
            self.coefficient.append(0)

    def predict(self,time):
        #some dp
        #if(time==0):
        #    return self.X[0]
        #if(time!=len(self.X)):
        #    XPrev = self.predict(time-1,self.static[0],self.static[1])
        #else:
        #    XPrev = self.X[time-1]
        if(time==0):
            return self.actual[0]
        XPrev=self.actual[time-1]
        #prediction
        XStatic = static(XPrev,self.static[0],self.static[1])
        XSeasonal = seasonal(XPrev,time,self.data,self.coefficient)
        #save data
        self.X.append(XStatic+XSeasonal)
        #return
        return XStatic+XSeasonal

    def cost(self,coefficient,time):
        return (self.actual[time]-self.predict(time))**2
    

    def train(self,period,startTime):
        for i in range(period):
            grad=nd.Gradient(seasonal)(self.coefficient,startTime+i)
        n=0
        for i in grad:
            self.coefficient[n]=self.coefficient[n]-i
            n+=1
        pass

    def __init__(self):
        #modify initial parameters here
        self.static=[1500,0.15] #k,rmax
        self.data=[]
        self.coefficient=[]
        self.actual=[]


arstneio = model()
arst=[]

for i in range(100):
    arst.append(arstneio.predict(i))

plt.plot(arst)
plt.show()
