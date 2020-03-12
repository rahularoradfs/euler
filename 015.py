# the problem of finding lattice paths
# corresponds to the problem of finding every sequence
# containing 20 Ds and 20 Rs, where each D = down, R = right

# This is a combinatorics problem - 
# which we can model as there being 40 spaces
# and we need to choose 20 of the 40 as Ds, filling the rest with Rs
# each of these is a unique choice
# by symmetry, we could also choose 20 of the 40 as Rs, filling the rest with Ds

# for the base case, 2 Ds and 2 Rs, the answer is 4c2 = 4! / 2! (4-2)! = 4 * 3 * 2 / (2 * 2) = 6

import math

def nCr(n, r): return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))
def grid(x, y): return int(nCr(x + y, x)) # this is the same as nCr(x + y, y) by symmetry

print(grid(2,2))
print(grid(20,20))
