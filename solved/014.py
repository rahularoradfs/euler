# dictionary of collatz sequence starting pts and lengths
cz_di = {1: 1, 2: 2}

def collatz(n):
	if n not in cz_di: 
		new_n = n // 2 if n % 2 == 0 else 3 * n + 1
		cz_di[n] = collatz(new_n) + 1
	
	return cz_di[n]

currmax = (1, 1)
for i in range(1, 1000000): 
	val = collatz(i)
	if val > currmax[1]: currmax = (i, val)
print(currmax)
