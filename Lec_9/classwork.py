import simprule as s
import math

def f(x):
    return math.log(x)
    #return 4*pow(x,3)

print("Area= ", s.simp(1,5,f,4))
print("From analytic calculation we get 4.04718956217")
