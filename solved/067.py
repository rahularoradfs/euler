# for this, you should work row-by-row
# there will be several possible ways to get to a number
# of these, only one way will have the maximum total
# store only that maximum total associated with it

# take the example four-row triangle provided
"""
   3
  7 4
 2 4 6
8 5 9 3
"""
# go row by row:
# row 1: only one way to get to 3, with total 3
# row 2: only one way to get to 7 and 4, totals 10 and 7 respectively
# row 3: only one way to get to 2 and 6, totals 12 and 13 respectively;
# 	 two ways to get to 4, totals 14 and 11; store only the 14 total
# row 4: only one way to get to 8 and 3, with totals 20 and 16 respectively
# 	 two ways to get to 5, totals 17 and 19; store only the 19 total
# 	 two ways to get to 9, totals 23 and 21; store only the 23 total
# solve: the maximum total on the final row is 23; output that alone

# can get to 2,1 by 1,1; 2,2 by 1,1
# 3,1 by 2,1; 3,2 by 2,1, 2,2; 3,3 by 2,2
# 4,1 by 3,1; 4,2 by 3,1, 3,2,; 4,3 by 2,2, 2,3; 4,4 by 2,3
# generally: index the triangle as [row][elem]
# can access [row][elem] via [row-1][elem-1] or [row-1][elem]
# only if they exist 

def max_weight(tri):
	max_tri = [None] * len(tri)
	for i, row in enumerate(tri):
		max_tri[i] = [None] * len(row)
		for j, elem in enumerate(row):
			if i > 0 and j > 0: rt1 = 0
			rt1 = max_tri[i-1][j-1] if i > 0 and j > 0 else 0
			rt2 = max_tri[i-1][j] if i > 0 and j < (len(row) - 1) else 0
			max_tri[i][j] = elem + max(rt1, rt2)
	return max(max_tri[-1])

def parse_text(input):
	return [[int(e) for e in row.strip().split(' ')] for row in input]

with open('067_input.txt', 'r') as tri:
	input = tri.readlines()

print('100-row triangle solution: {}'.format(max_weight(parse_text(input))))
