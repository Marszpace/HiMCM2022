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
        data=[]
        n=0
        
        for i in data:
            df=pd.read_csv(i)
            self.data.append(df.values.tolist())
            self.coefficient.append(0)

    def predict(self,time):
        if(time==0):
            return self.X[0]
        if(time!=len(self.X)):
            XPrev = self.predict(time-1,k)
        else:
            XPrev = self.X[time-1]
        XStatic = static(XPrev,self.static[0],self.static[1])
        XSeasonal = seasonal(XPrev,time,self.data,self.coefficient)
        self.X.append(XStatic+XSeasonal)
        return XStatic+XSeasonal

    def train(self,period,time):
        #Only this part is left
        pass

    def __init__(self,x0,k,rmax):
        self.X=[x0]
        self.static=[k,rmax]
        self.data=[]
        self.coefficient=[]
        self.actual=[]

k=1500
rmax=0.15
arstneio = model(0.03,k,rmax)
arst=[]

for i in range(100):
    #print(arstneio.predict(i,k))
    arst.append(arstneio.predict(i))
    #k-=10

plt.plot(arst)
plt.show()