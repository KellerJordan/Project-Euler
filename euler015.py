from math import factorial

for _ in range(int(input().strip())):
    i = input().strip().split(' ')
    n, m = int(i[0]), int(i[1])
    print(factorial(n + m) // (factorial(n) * factorial(m)) % (10**9 + 7))
