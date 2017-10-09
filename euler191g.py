# solution to a generalized version of project euler problem 191
# includes number of late days parameter
# by default, this is equal to one as in the problem

def dyn_dec(func):
    R = {}
    def dyn_wrap(*args):
        k = str(args)
        if k not in R:
            R[k] = func(*args)
        return R[k]
    return dyn_wrap

# fnl(): returns the number of prize strings given parameters
# n: string length, l: lates remaining (do not all have to be used)
@dyn_dec
def fnl(n, l):
    if l < 0: # used too many L's. invalid string
        return 0
    elif n <= 2: # not enough spaces to make AAA, so allow all possible strings
        if l >= n: # plenty of L's left, so 3^n possible
            return 3**n
        elif l == 0: # no L's left, so 2^n possible
            return 2**n
        else: # must be that n = 2, l = 1
            return 8
    else:
        # by ending each substring with either O or L, any substring can occur next
        # so just sum over the possibilities
        O = fnl(n-1, l)
        AO = fnl(n-2, l)
        AAO = fnl(n-3, l)
        L = fnl(n-1, l-1)
        AL = fnl(n-2, l-1)
        AAL = fnl(n-3, l-1)
        return O + AO + AAO + L + AL + AAL

N, L = 30, 1 # default case
# N, L = 10000, 100 # can handle up to around here
[fnl(n, L) for n in range(N)] # use bottom up DP to avoid exceeding recursion depth
print(fnl(N, L))
