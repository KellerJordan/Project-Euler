def palgen():
    P = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            p = i * j
            if p > 101100 and str(p) == str(p)[::-1]:
                P.append(p)
    return P

P = palgen()
for _ in range(int(input().strip())):
    n, m = int(input().strip()), 0
    for p in P:
        if p > m and p < n:
            m = p
    print(m)
