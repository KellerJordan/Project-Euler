from math import sqrt
import time

def pent(num):
    return num*(3*num-1)*.5

def isPent(num):
    t1=sqrt(1+24*num)
    if(not t1.is_integer()):
        return False
    else:
        return ((1+t1)/6).is_integer()
    
def testPair(num1,num2):
    t1=isPent(num1-num2)
    if(not t1):
        return False
    elif(isPent(num1+num2)):
        return True
    
def findPair(to):
    start=time.time()
    for n1 in range(to):
        for n2 in range(n1):
            num1=n1+1
            num2=n2+1
            if(testPair(pent(num1),pent(num2))):
                end=time.time()
                print('works for %s %s' % (num1,num2))
                print('took %s seconds' % (end-start))
                return True
    return False

findPair(3000)
print(pent(2167)-pent(1020))
