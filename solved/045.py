def T(n): return n * (n + 1) / 2
def P(n): return n * (3*n - 1) / 2
def H(n): return n * (2*n - 1)

n = 1
T_curr, P_curr, H_curr = 0, 0, 0
T_n, P_n, H_n = 0, 0, 0
excl_list = [1, 40755]
for T_n in range(1, 1000000):
	T_curr = T(T_n)
	if T_curr > P_curr: 
		P_n += 1
		P_curr = P(P_n)
	if T_curr > H_curr:
		H_n += 1
		H_curr = H(H_n)
	if T_curr == P_curr and T_curr == H_curr and T_curr not in excl_list:
		print(int(T_curr))
		break
