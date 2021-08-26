import numpy as np
import matplotlib.pyplot as plt
from math import factorial, log as ln


t = []
v = []
infile = open("running.txt","r")
for line in infile:
    tnext, vnext = line.strip().split(",")
    t.append(float(tnext))
    v.append(float(vnext))
infile.close()


def dv(x,y):
    dv=[0]
    for i in range(1,len(x)):
        dv.append((y[i]-y[i-1])/(x[i]-x[i-1]))
    plt.plot(x,dv)
    plt.title("akselrasjonen pr tid a(t)")
    plt.xlabel("tid")
    plt.ylabel("akslerasjon")
    plt.show()

def distanse(x,y):
    s=[0]
    for i in range(0,len(y)-1):
        s.append(s[i]+(0.5*((t[i+1]-t[i])*(v[i+1]+v[i])))) #trapesmetoden
    plt.plot(t,s)
    plt.title("strekning tilbakelagt S(t)")
    plt.xlabel("tid")
    plt.ylabel("distanse")
    plt.show()
    print(f"distansen som ham har løpt er: {s[-1]}")

(dv(t,v))
distanse(v,t)
