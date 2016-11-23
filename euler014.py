def collatz(n):
    l = 0
    P = {}
    while n != 1:
        if n in C:
            l += C[n]
            break
        if n < N:
            P[n] = -1 * l
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l += 1
    for k in P:
        C[k] = P[k] + l

N, C, M, m = 5 * 10**6, {}, list(), 0
M.append(1)
for n in range(2, N):
    if not n in C:
        collatz(n)
    if C[n] >= m:
        M.append(n)
        m = C[n]

for _ in range(int(input().strip())):
    n = int(input().strip())
    for m in M:
        if m > n:
            break
        t = m
    print(t)
           
