def dA(a,b,f):
    return (b-a)/6*(f(a)+4*f((a+b)/2)+f(b))

def simp(a,b,f,n):
    #print("Given: a= ",a,"   b= ",b,"  f=",f,"   n=",n)

    sum=0
    dn=(b-a)/n
    for i in range(0,n):
        sum+=dA(a+(b-a)*i/n,a+(b-a)*(i+1)/n,f)

    #print("sum= ",sum)
    return sum

#def f(x):
#    return 1

#simp(0,10,f,100)
