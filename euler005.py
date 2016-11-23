from math import floor, log

def pgen():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

for _ in range(int(input().strip())):
    n, P = int(input().strip()), pgen()
    r, f = 1, next(P)
    while(f <= n):
        r *= f ** floor(log(n, f))
        f = next(P)
    print(r)
