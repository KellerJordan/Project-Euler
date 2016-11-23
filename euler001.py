def multsum(n, x):
    o = n // x
    return (x * o * (o + 1)) >> 1

for _ in range(int(input().strip())):
    n = int(input().strip()) - 1
    print(multsum(n, 3) + multsum(n, 5) - multsum(n, 15))
