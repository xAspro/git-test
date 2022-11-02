import numpy as np
import matplotlib.pyplot as plt

def fn(x):
    return x*x-10

def der(x):
    return 2*x

def NR(a,e):
    t=[]
    f=[]
    
    x=a;
    while (abs(fn(x))>e):
        t.append(x)
        f.append(fn(x))
        x=x-fn(x)/der(x)

        

    t.append(x)
    f.append(fn(x))
    
    print(t)
    print(f)
    plt.plot(t,label="Newton Raphson")
    plt.legend()
    plt.show()

NR(0.1,0.00001)
