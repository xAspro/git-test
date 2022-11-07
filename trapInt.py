def dA(a,b,f):
    return (f(b)+f(a))/2*(b-a)

def iter(a,b,f,n):
    sum=0
    print("in Trap")

    for i in range(0,n):
        m=a+(b-a)*i/n
        sum+=dA(m,(m+(b-a)/n),f)

    return sum
