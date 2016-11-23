def euler(n, k):
    l, m = len(n), 0
    for i in range(l - k):
        p = 1
        for j in range(k):
            p *= int(n[i + j])
        if p > m:
            m = p
    return m

for _ in range(int(input().strip())):
    k = int(input().strip().split(' ')[1])
    n = input().strip()
    print(euler(n, k))
