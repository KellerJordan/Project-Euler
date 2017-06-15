# solution file for project euler problem 173

# Every lamina can be divided into four quadrants of area a*b. Every unique 
# a,b pair represents one unique lamina. So, a*b<=n//4. Define m=n//4. To 
# find the number of valid pairs, observe that for each value of 0<a<sqrt(m) 
# there are m//a unique b's that satisfy a*b<=m, a-1 duplicates from previous 
# iterations, and one b=a which is invalid. So, we have
#           valid b's given a = m//a - (a-1) - 1 = m//a - a.

from math import sqrt, ceil

m = int(input()) // 4
print(sum(m//a - a for a in range(1, ceil(sqrt(m)))))

# or, taking out the a from the summation (slightly faster, more verbose):
# high = ceil(sqrt(m)) - 1
# count = sum(m//a for a in range(1, high + 1))
# count -= high * (high + 1) // 2
# print(count)
