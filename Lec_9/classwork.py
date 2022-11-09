import simprule as s

def f(x):
    return 10-3*x*x

print("Area= ", s.simp(-1,3,f,4))
print("From analytic calculation we get 12")  #10x-x^3  =  30-27--10---1 =12
