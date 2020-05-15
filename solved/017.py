worddi = {
	0: '',
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven', 
	12: 'twelve', 
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen', 
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty', 
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	1000: 'one thousand',
} 

def num2word(n):
	if 0 <= n <= 19: return worddi[n]
	elif 20 <= n <= 99: return worddi[n // 10 * 10] + '-' + worddi[n % 10]
	elif 100 <= n <= 999: return worddi[n // 100] + ' hundred' + (' and ' + num2word(n % 100) if n % 100 != 0 else '')
	elif n == 1000: return worddi[n]

print(sum(sum(j.isalpha() for j in num2word(i)) for i in range(1,1001)))
