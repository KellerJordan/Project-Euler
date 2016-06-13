import time
def multsum(n,x):
    o=(n-.1)//x
    return x*o*(o+1)/2
def multssum(n,x,y):
    start=time.time()
    print(multsum(n,x)+multsum(n,y)-multsum(n,x*y))
    print(time.time()-start)
multssum(1000,3,5)
