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

P, Pgen = [], pgen()
for n in range(10001):
    P.append(next(Pgen))

for _ in range(int(input().strip())):
    print(P[int(input().strip()) - 1])
