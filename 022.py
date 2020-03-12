# read in input file and sort
import csv
with open('022_input.txt', newline = '') as input:
	names = sorted(list(csv.reader(input, delimiter = ',', quotechar = '"'))[0])

# compute character sum of each name
def score(name): return sum( (ord(char) - 64 for char in name) )

# compute character sum, multiply it by its position, and output the sum of that
print( sum( ( (i + 1) * score(name) for i, name in enumerate(names) ) ))
