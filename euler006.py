for _ in range(int(input().strip())):
    n = int(input().strip())
    s1 = (n * (n + 1) // 2) ** 2
    s2 = (n * (n + 1) * (2 * n + 1)) // 6
    print(s1 - s2)
