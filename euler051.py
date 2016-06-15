import math
import time

primes=[2]
otherprimes={}
otherprimes[2]=True
def createprimelist(n):
    start=time.time()
    i=3
    while i<n:
        if isprime(i):
            primes.append(i)
            otherprimes[i]=True
        i+=2
    print('time to generate list:',time.time()-start)
def isprime(n):
    prime=2
    i=0
    rtn=math.sqrt(n)
    while prime<=rtn:
        if n%prime == 0 :
            return False
        prime=primes[i]
        i+=1
    return True


def isalreadyprime(n):
    if n in otherprimes:
        return True
    return False

def testprimecase(n,a,goal):
    li=list(str(n))
    le=len(li)
    v=0
    failed=0
    if a&(1<<(le-1)):
        v=1
        failed=1
    while v<10:
        i=0
        while i<le:
            if a&(1<<i):
                li[le-i-1]=str(v)
            i+=1
        if not isalreadyprime(int(''.join(li))):
            failed+=1
            if failed>10-goal:
                return False
        v+=1
    return True

def testprime(n,goal):
    p=1<<(len(str(n)))
    d=2
    while d<p:
        if testprimecase(n,d,goal):
            return True
        d+=2
    return False

def findsolution(goal):
    start=time.time()
    for n in primes:
        if testprime(n,goal):
            print('time to find:',time.time()-start)
            return n
    print(time.time()-start)

createprimelist(1000000)
print(findsolution(8))
