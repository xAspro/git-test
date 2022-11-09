import simprule as s
import numpy as np
import math

def f(x):
    return 2/math.sqrt(math.pi)*math.exp(-x*x)

print("Area= ", s.simp(0,1,f,100))

print("From wikipedia https://en.wikipedia.org/wiki/Romberg's_method , the value actual value for err function from 0 to 1 is approximately 0.842700792949715 and our answer is nearby")
