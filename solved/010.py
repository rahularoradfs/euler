import math

def Sieve(n):
	# start saying everything is prime
	# go to two
	# knock off all multiples of two 
	# go to the next prime
	# knock off all of its multiples
	# etc...
	# until you hit n/2
	
	primes = {i: True for i in range(2, n)}
	
	for i in range(2, math.floor(n ** (1/2)) + 1): 
		if primes[i] == True:
			for j in range(2*i, n, i):
				primes[j] = False
	return primes

primes = Sieve(2000000)
print(sum( (i for i in primes if primes[i] == True) ))
