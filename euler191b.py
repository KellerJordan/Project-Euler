results = {}

def t(n):
    if (n <= 0): return 1

    if n in results: return results[n]
    
    count = t(n - 2) + t(n - 1)
    if (n > 1): count += t(n - 3)

    results[n] = count
    return count

def T(n):
    count = t(n)
    for i in range(n): count += t(i) * t(n - 1 - i)
    return count

print(T(30))
