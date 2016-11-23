from math import sqrt

def euler(n):
    d, f = 2, 2
    while d <= sqrt(n):
        while n % d == 0:
            n //= d
            f = d
        d += 1
    return n if n > f else f   

for _ in range(int(input().strip())):
    print(euler(int(input().strip())))
