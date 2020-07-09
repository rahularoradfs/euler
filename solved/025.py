phi = (1 + 5 ** 0.5) / 2

def fib(n, di = {0: 0, 1: 1}):
	if n not in di: 
		di[n] = fib(n - 1) + fib(n - 2)
	return di[n]

# by the closed form expression of fibonnaci numbers, 
# this has 1000 digits when log(fib(n)) / log(10) > 999
# and grows roughly with O(phi ^ n)
# so we need roughly n log phi / log 10 > 999
# or n > 999 log 10 / log phi 
# we are likely off by a couple here - let's seach in a range around our bound

from math import log, floor

approx = floor(999 * log(10) / log(phi))

# memoize 
[fib(i) for i in range(approx - 5)]

for n in range(approx - 5, approx + 5):
	order_mag = log(fib(n)) / log(10)
	if order_mag > 999:
		print(f"fib({n}) is the first to have {floor(order_mag) + 1} digits; your approximation was {approx}")
		break
