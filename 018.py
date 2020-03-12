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


