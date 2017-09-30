def dynamic_decorator(func):
    results = {}
    def wrapper(arg):
        if arg in results:
            return results[arg]
        else:
            return func(arg)
    return wrapper

m = 2
# m = 15

def pfailure(s):
    # pfailure(s-m)
    ...



# pfailure(s) =
# 1 if s < 0(or m) else
# sum for n = 1->inf of
# .5^n * pfailure(s-m + 2^(n-1))
