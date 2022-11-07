import math
import numpy as np

import leftRuleInt as l
import rightRuleInt as r
import midRuleInt as m
import trapInt as t

def f(x):
    return np.sin(x)

def f2(x):
    return 10-x*x

b=3/4*math.pi
n=1000

print("left point")
L=l.iter(0,b,f,n)
print(L)
print("E= ",abs(L-(1+1/math.sqrt(2))))

print("right point")
R=r.iter(0,b,f,n)
print(R)
print("E= ",abs(R-(1+1/math.sqrt(2))))

print("mid point")
M=m.iter(0,b,f,n)
print(M)
print("E= ",abs(M-(1+1/math.sqrt(2))))

print("trap")
T=t.iter(0,b,f,n)
print(T)
print("E= ",abs(T-(1+1/math.sqrt(2))))


print("For f(x)=10-x^2 in [-2,2]: ")
print(t.iter(-2,2,f2,n))
