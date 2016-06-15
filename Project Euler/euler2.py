import time

def sum1(n):
    f=1
    g=1
    h=0
    s=0
    start=time.time()
    while f<n:
        h=g
        g=f
        f+=h
        if f%2==0:
            s+=f
    print(time.time()-start)

def sum2(n):
    e=0
    o=1
    s=0
    start=time.time()
    while(e<n):
        s+=e
        o2=o
        o+=2*e
        e=3*e+2*o2
    print(time.time()-start)

sum1(10**20000)
sum2(10**40000)
