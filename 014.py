# dictionary of collatz sequence starting pts and lengths
cz_di = {1: 1, 2: 2}

def collatz(n, length):
	"""
	takes a number n
	and the length l of the sequence leading to that n
	and return the length of the collatz seq
	that starts with n
	"""
	
	# if n is in the dict: return it 
	if n in cz_di: return cz_di[n]
	
	# calculate a new n by the collatz rules
	new_n = n // 2 if n % 2 == 0 else 3 * n + 1

	# see if it's in the dictionary:
	if new_n in cz_di:
		# if so, the length of this seq
		# should be the length of the prev plus one
		cz_di[n] = cz_di[new_n] + 1 
		return cz_di[n]

	# if not, return the collatz value of the new item
	# passing in a larger length
	else:
		return collatz(new_n, length + 1)

for i in range(1, 1000000): collatz(i, 1)

print("""f(1) = {0} should be 1
f(20) = {1} should be 8
f(1005) = {2} should be 68
f(2 ^ 16) = {3} should be 17
f(19797) = {4} should be 31
""".format(cz_di[1], cz_di[20], cz_di[1005], cz_di[2**16], cz_di[19797]))

mod_di = {i: cz_di[i] for i in cz_di if i < 1000000}
maxkey = max(cz_di, key = cz_di.get)
print(maxkey)
print(cz_di[maxkey])
