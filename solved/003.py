import math

n = 600851475143

# recursively generate the prime factors of n
def factorize(a):
	factors = set()
	for i in range(2, math.floor(a ** 1/2) + 1):
		if a % i == 0: return factors.union(factorize(a / i), factorize(i))
	return {int(a)}

print(max(factorize(n)))
