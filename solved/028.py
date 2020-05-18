size = 1001
n = 1
sum = 1
for step in range(1, (size - 1)//2 + 1):
	for i in range(4):
		n += step * 2
		sum += n
print(sum)
