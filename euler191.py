"""
To compute the number of possible strings of length n, we define recursive function T(n) which
counts the number of prize strings of length n containing only the characters A and O. For n >= 3,
we have three options for the start of the string: 'AAO', 'AO', or 'O', each of which able to
subsequently branch into any of the three. For n <= 2, any string is possible so we have:

T(n) = { 2^n                        if n <= 2
       { T(n-1) + T(n-2) + T(n-3)   else

When there is an L at position i, the total number of strings is the product of the number of
possibilities before the L and the number after. We sum over all possible positions of L, and the
situation where there are no Ls to get the result.
"""

R = {} # dict for memoization
# T(n): counts number of prize strings containing O, A of length n
def T(n):
    if n not in R:
        R[n] = 2**n if n < 3 else T(n-1) + T(n-2) + T(n-3)
    return R[n]

N = 30 # default case
# N = 30000 # can handle up to around here
[T(n) for n in range(N)] # do bottom up DP to avoid exceeding recursion depth
print(T(N) + sum(T(i) * T(N-1-i) for i in range(N)))
