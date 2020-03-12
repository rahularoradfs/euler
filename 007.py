
primes = [2]

i = 3
ln = 1
while ln < 10001:
	for p in primes:
		if p > i/2:
			ln += 1
			primes.append(i)
			break 
		if i % p == 0: break
	i += 2

print(primes[10000])
