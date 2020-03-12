import collections
import math
import operator
from functools import reduce 
factors = collections.Counter()

def factorize(a):
	for i in range(2, math.floor(a ** (1/2)) + 1):
		if a % i == 0: return factorize(i) + factorize(a/i)
	return collections.Counter([a,1])

for i in range(1, 21): factors = factors | factorize(i)

print(factors)
print(reduce(operator.mul, (i ** factors[i] for i in factors), 1))
