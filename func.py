import numpy as np

def square(a):
    return a**2;


a=float(input('Enter a number:'))
print('Square of the number = ',square(a))

b=np.array([1,3,5])
print("Square of a list = ", square(b))

c=np.array([1,2,"g"])
#print("list c=",c,"      square of c(will give an error!!)= ",square(c))

d=[1,2,3]
#print("d= ",d,"  sq of d=",square(d))

e=[1,2,3,'helloworld']
#print('e= ',e,"  sq of e=",square(e))

