from numpy import *
import math
def loadTxtData(path):
    fr, ls = open(path), []
    for line in fr.readlines():
        lineArr, floatline = line.strip().split(), []
        for item in lineArr:
            floatline.append(float(item))
        ls.append(floatline)
    fr.close
    return ls

def d(x,X,S,p):
    a=x-X
    s=linalg.det(S)
    d=a*linalg.inv(S)*a.T+math.log(s)-2*math.log(p)
    return d

def P1(x):
    P=math.exp(-0.5*d(x,x1,S1,p1))/math.exp(-0.5*d(x,x1,S1,p1))+math.exp(-0.5*d(x,x2,S2,p2))
    return P
def P2(x):
    P=math.exp(-0.5*d(x,x2,S2,p2))/math.exp(-0.5*d(x,x1,S1,p1))+math.exp(-0.5*d(x,x2,S2,p2))
    return P

path1,path2= 'D:/Information science/Bayes5_1_1.txt','D:/Information science/Bayes5_1_2.txt'
a,b=mat(loadTxtData(path1)),mat(loadTxtData(path2))
x1,x2=mean(a, axis=0),mean(b, axis=0)
S1,S2=cov(a.T),cov(b.T)
p1,p2=6/14,8/14
for i in range(6):
    print(i+1,end=' ')
    if(P1(a[i])>P2(a[i])):
        print("总体为G1，判入G1")
    else:
        print("总体为G1，判入G2")
    print(P1(a[i]),P2(a[i]))
for i in range(8):
    print(i + 7, end=' ')
    if(P1(b[i])>P2(b[i])):
        print("总体为G2，判入G1")
    else:
        print("总体为G2，判入G2")

for i in range(6):
    y=delete(a,i,axis=0)
    d1=d(a[i],mean(y),cov(y.T),p1)
    d2=d(a[i],x2,S2,p2)
    if (d1>d2):
        print("总体为G1，判入G1")
    else:
        print("总体为G1，判入G2*")
for i in range(8):
    y=delete(b,i,axis=0)
    d1=d(b[i],mean(y),cov(y.T),p2)
    d2=d(b[i],x1,S1,p1)
    if (d1>d2):
        print("总体为G2，判入G2")
    else:
        print("总体为G2，判入G1*")