import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
        if(time==0):
            return self.X[0]
        if(time!=len(self.X)):
            XPrev = self.predict(time-1,self.static[0],self.static[1])
        else:
            XPrev = self.X[time-1]
        #prediction
        XStatic = static(XPrev,self.static[0],self.static[1])
        XSeasonal = seasonal(XPrev,time,self.data,self.coefficient)
        #save data
        self.X.append(XStatic+XSeasonal)
        #return
        return XStatic+XSeasonal

    def train(self,period,time):
        #Only this part is left
        pass

    def __init__(self,x0):
        #modify initial parameters here
        self.X=[x0]
        self.static=[1500,0.15] #k,rmax
        self.data=[]
        self.coefficient=[]
        self.actual=[]


arstneio = model(0.03)
arst=[]

for i in range(100):
    arst.append(arstneio.predict(i))

plt.plot(arst)
plt.show()
