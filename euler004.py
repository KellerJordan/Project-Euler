def ispalindrome(n):
    if str(n)[::-1]==str(n):
        return True
    return False
def euler(v):
    m=0
    for a in range(v):
        for b in range(v):
            if ispalindrome(a*b) and a*b>m:
                m=a*b
    return m

print(euler(999))
