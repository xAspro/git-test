def dA(a,b, f):
    return f(a)*(b-a)

def iter(a,b,f,n):
    sum=0
    print("int mid")
    for i in range(0,n):
        m=a+(b-a)*(i+0.5)/n
        sum+=dA(m,m+(b-a)/n,f)

    return sum

