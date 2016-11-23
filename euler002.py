def fibgen():
    a, b = 0, 2
    while True:
        yield a
        a, b = b, a + 4 * b

for _ in range(int(input().strip())):
    n, s, f, F = int(input().strip()), 0, 0, fibgen()
    while(f <= n):
        s += f
        f = next(F)
    print(s)
