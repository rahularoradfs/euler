# with Euler's formula, you can generate pythagorean triples
# with pairs of integers m, n where m > n > 0
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2 
# to generate all such pairs, insert an integer factor k

# with this, we have a + b + c = k(2m^2 + 2mn) = 1000
# or, equivalently, k(m^2 + mn) = 500 for m > n 
# so we need to find m where (500 - m^2) is equal to mn
# and where n < m 

import math
for m in range(1, math.floor(500 ** (1/2)) + 1):
	LHS = 500 - m ** 2
	if LHS % m == 0: # if 500 - m ** 2 is divisible by m:
		n = LHS // m
		if m > n:
			print('m: {0}, n: {1}'.format(m, n))
			a, b, c = m**2-n**2, 2*m*n, m**2+n**2
			print('{0}^2 + {1}^2 = {2}^2'.format(a,b,c))
			print('abc = {0}'.format(a*b*c))
			break
