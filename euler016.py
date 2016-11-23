for _ in range(int(input().strip())):
    s = 0
    for c in str(1 << int(input().strip())):
        s += int(c)
    print(s)
