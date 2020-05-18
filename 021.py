from math import floor, sqrt

def divisors(n):
	divisors = []
	for i in range (1, floor(sqrt(n)) + 1):
		if n % i == 0: 
			divisors.append(i)
			if i != 1 and i != sqrt(n):
				divisors.append(n // i)
	return divisors

divdict = {i: sum(divisors(i)) for i in range(10000)}
amiable = dict(filter(lambda item: item[1] != item[0] and divdict.get(item[1],0) == item[0], divdict.items()))
print(sum(amiable.keys()))
