import numpy as np

x=np.linspace(0,2*np.pi,100);
y=np.cos(x)

for i in range(len(x)):
    print(x[i],y[i])
