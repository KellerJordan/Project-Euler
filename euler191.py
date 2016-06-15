def euler(n):
    """case with no L's"""
    r=2**n
    r-=sumial(n)
    """cases with 1 L"""
    p=0
    while p<n:
        q=n-p-1
        r+=(2**p-sumial(p))*(2**q-sumial(q))
        p+=1
    return r
sumials={}
def sumial(n):
    if n in sumials:
        return sumials[n]
    if n<3:
        return 0
    answer=2**(n-3)+sumial(n-3)+sumial(n-2)+sumial(n-1)
    sumials[n]=answer
    return answer

print(euler(30))
