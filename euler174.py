# sieve which gets number of divisors of each number
def factor_sieve(limit):
    f = [1] * (limit+1)
    f[0] = f[1] = 0

    for (i, factors) in enumerate(f):
        if factors != 0: # if >=2, find every number which is a multiple
            for n in range(i*(i+1), limit+1, i): # don't increment i^2 because that is equiv to b=0 which is invalid
                f[n] += 1
    return f

N = 1000000
F = factor_sieve(N//4)
L = [0, 0]
for (i, f) in enumerate(F[2:]):
    L.append(L[-1])
    if f <= 10:
        L[-1] += 1

for _ in range(int(input())):
    k = int(input())
    print(L[k//4])
