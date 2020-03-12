fib_di = {}
def fib(i):
	if i == 0: fib_di[i] = 1
	elif i == 1: fib_di[i] = 2
	else: fib_di[i] = fib_di[i-1] + fib_di[i-2]
	return fib_di[i]

sum = 0
i = 0
while True:
	f_i = fib(i)
	if f_i > 4 * 10**6: break
	if f_i % 2 == 0: sum += f_i 
	i += 1

print(sum)
