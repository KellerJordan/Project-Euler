# find smallest number with 2^500500 divisors
# return modulo 500500507

m = 500500507
d = 500500

def prime_sieve():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q**2] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            del D[q]
        q += 1

# smallest with 1 factor
num = 1

P = prime_sieve()
primes = {2: 2}
next(P)
for _ in range(d):
    # how to compare without saving full value? just save modulo value?
    p = min(primes, key=lambda p: primes[p])
    res = p * primes[p]**2
    primes[p] = res

