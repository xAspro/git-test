import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,100)
y=np.loadtxt('1.txt')

fig,ax=plt.subplots(1,2)

ax[0].plot(x,np.sin(x),label='sin(x)')
ax[0].plot(y[:,0],y[:,1],label='cos x')

ax[0].set_xlabel("Angle in rad")
ax[0].set_ylabel('sinx/cosx')
ax[0].set_title('sinx vs cosx')
ax[0].legend()

ax[1].plot(np.random.rand(1000),np.random.rand(1000),"r*")
plt.show()
