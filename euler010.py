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

S, P, s, p = {}, pgen(), 0, 0
while p < 1000000:
    p = next(P)
    s += p
    S[p] = s

for _ in range(int(input().strip())):
    n = int(input().strip())
    while S.get(n) == None:
        n -= 1
    print(S.get(n))
