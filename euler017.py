from math import floor, log

def single(n):
    if n == 1: return "One "
    if n == 2: return "Two "
    if n == 3: return "Three "
    if n == 4: return "Four "
    if n == 5: return "Five "
    if n == 6: return "Six "
    if n == 7: return "Seven "
    if n == 8: return "Eight "
    if n == 9: return "Nine "
    return ""

def double(n):
    if n < 10: return single(n)
    if n < 20:
        if n == 10: return "Ten "
        if n == 11: return "Eleven "
        if n == 12: return "Twelve "
        if n == 13: return "Thirteen "
        if n == 14: return "Fourteen "
        if n == 15: return "Fifteen "
        if n == 16: return "Sixteen "
        if n == 17: return "Seventeen "
        if n == 18: return "Eighteen "
        if n == 19: return "Nineteen "
    t, r = int(str(n)[0]), ""
    if t == 2: r = "Twenty "
    if t == 3: r = "Thirty "
    if t == 4: r = "Forty "
    if t == 5: r = "Fifty "
    if t == 6: r = "Sixty "
    if t == 7: r = "Seventy "
    if t == 8: r = "Eighty "
    if t == 9: r = "Ninety "
    return r + single(int(str(n)[1]))

def suffix(p, t):
    if int(t) == 0: return ""
    if p == 3: return "Thousand "
    if p == 6: return "Million "
    if p == 9: return "Billion "
    if p == 12: return "Trillion "
    return ""

for _ in range(int(input().strip())):
    n, r, p = input().strip(), "", 0
    while p < len(n):
        a, b = len(n) - p - 3, len(n) - p
        if a < 0: a = 0
        t = str(int(n[a : b]))
        r = suffix(p, t) + r
        if len(t) == 3:
            r = single(int(t[0])) + "Hundred " + double(int(t[1 : 3])) + r
        if len(t) == 2:
            r = double(int(t[0 : 2])) + r
        if len(t) == 1:
            r = single(int(t[0])) + r
        p += 3
    print(r)