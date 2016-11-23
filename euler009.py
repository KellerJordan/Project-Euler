def euler(n):
    m = -1
    for a in range(1, n // 3):
        b = n * (n - 2 * a) / (2 * n - 2 * a)
        if b.is_integer():
            c = n - a - b
            p = a * b * c
            if p > m: m = p
    return m

for _ in range(int(input().strip())):
    print(int(euler(int(input().strip()))))
