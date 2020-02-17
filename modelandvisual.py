#Leyton Taylor Lab 1
import random
import matplotlib.pyplot as plt

def genOrbits():
    Fout=dict()
    Gout=dict()
    Dout=dict()
   
    randomFseeds=[random.uniform(-1.99,1.99) for k in range(10)]
    randomGseeds=[random.uniform(-1.99,1.99) for k in range(10)]
    randomDseeds=[random.random() for k in range(10)]
    
    Fout={x:F(x) for x in randomFseeds}
    Gout={x:G(x) for x in randomGseeds}
    Dout={x:D(x) for x in randomDseeds}
    
    print("F seeds: "+str(randomFseeds)+'\n'
          +"G seeds: "+str(randomGseeds)+'\n'
          +"D seeds: "+str(randomDseeds))
    
    return Fout,Gout,Dout
    
##x belongs to [0,1)
def F(x):
    outList=[(0,x)]
    temp=x
    for i in range(1,100):  
        lastOut=temp**2-2
        temp=lastOut
        outList.append((i,temp))
    return outList

##c<-2, -2<x<2
def G(x):
    outList=[(0,x)]
    temp =x
    for i in range(1,100):
        lastOut=temp**2-20
        temp=lastOut
        outList.append((i,temp))
    return outList

##0<=x<1
def D(x):
    outList=[(0,x)]
    temp=x
    for i in range(1,100):
        if(temp<.5 and temp>=0):
            lastOut=temp*2
            temp=lastOut
            outList.append((i,temp))
        else:
            lastOut=temp*2-1
            temp=lastOut
            outList.append((i,temp))
            
    return outList

##Creates a plot of the orbit and seed
def plotLine(orbitDict,seed):
    plt.ylabel='Output of Iteration'
    
    xAxis=[orbitDict[seed][n][0] for n in range(100)]
    yAxis=[orbitDict[seed][n][1] for n in range(100)]

    
    plt.plot(xAxis,yAxis)
    plt.show()

    
##Plots a visualization of the period
def plotPeriod(orbitDict,seed):
    xAxis=[]
    yAxis=[]
    
    for k in orbitDict[seed]:
        if(k[1]==seed):
            yAxis.append(seed)
            xAxis.append(k[0])
            
    plt.plot(xAxis,yAxis, 'ro')
    plt.axis([0,100,-2,2])
    plt.show()
    



