# solution to project euler problem 191

# To compute the number of possible strings of length n,
# we define recursive function T(n) which counts the
# number of prize strings of length n. For large enough
# n, we have three options for the start of the string:
# 'AAO', 'AO', or 'O', each of which can have any
# of the options afterwards. If n=2, then there are 4
# possible strings, if n=1 there are 2, and if n=0 there
# is only one: no character. So, we have the following:
# T(n) = { 1                        if n=0
#        { 2                        if n=1
#        { 4                        if n=2
#        { T(n-1) + T(n-2) + T(n-3) else


# dynamic dict of results of t(n)
results = {}

# T(n), counts number of prize strings of length n
def T(n):
    if (n < 3): return 2 ** n # shorthand for base cases
    if n in results: return results[n]
    count = T(n - 1) + T(n - 2) + T(n - 3)
    results[n] = count
    return count

n = 3000
print(T(n) + sum(T(i) * T(n - 1 - i) for i in range(n)))
