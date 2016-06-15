from math import sqrt

def euler(n):
    v=1
    for f in pfactors(n):
        if not pfactors(f):
            v=f
    return v

def pfactors(n):
    factors=[]
    i=3
    sqn=sqrt(n)
    while i<=sqn:
        if not n%i:
            factors.append(i)
        i+=2
    return factors

print(euler(600851475143))
