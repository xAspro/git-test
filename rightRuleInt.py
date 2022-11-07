def dA(a,b, f):
    return f(a)*(b-a)

def iter(a,b,f,n):
    sum=0
    print("In righ")
    for i in range(1,n+1):
        m=a+(b-a)*i/n
        sum+=dA(m,m+(b-a)/n,f)
    
    return sum

