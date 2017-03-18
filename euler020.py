for _ in range(int(input())):
    n = int(input())
    f = 1
    for i in range(1, n + 1):
        f *= i
    f = str(f)
    s = 0
    for i in range(len(f)):
        s += int(f[i])
    print(s)