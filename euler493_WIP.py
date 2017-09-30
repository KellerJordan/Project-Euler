# why doesn't this work?

from scipy.misc import comb

def pr_at_most_n_colors(n):
    res = comb(7, n)
    for i in range(20):
        res *= (n*10-i) / (70-i)
    return res

def pr_n_colors(n):
    return pr_at_most_n_colors(n) - pr_at_most_n_colors(n-1)

def avg_colors():
    return sum([n * pr_n_colors(n) for n in range(8)])

print(sum([pr_n_colors(n) for n in range(8)]))
print(avg_colors())
