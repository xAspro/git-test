def dA(a,b,f):
    #print("Given: a= ",a,"   b= ",b,"  f=",f)
    #print("f(a)= ",f(a),"  f(b)= ",f(b),"   f((a+b)/2)= ",f((a+b)/2))
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6

def simp(a,b,f,n):
    #print("Given: a= ",a,"   b= ",b,"  f=",f,"   n=",n)

    sum=0
    dn=(b-a)/n
    for i in range(0,n):
        dS=dA(a+dn*i,a+dn*(i+1),f)
        #print("dS= ",dS)
        sum+=dS

    #print("sum= ",sum)
    return sum

#def f(x):
#    return 1
#
#print("for f(x)=1: ", simp(0,10,f,10))
