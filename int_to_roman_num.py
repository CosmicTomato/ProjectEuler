#takes in an integer and returns a roman numeral (string of letters)
#output is in form of string, with letters separated by commas

#returns 'optimal' form of number
#see https://projecteuler.net/about=roman_numerals for criteria

def main( n ):

	n = int( n )

	ans = []

	while n >= 1000:
		ans.append( 'M' )
		n -= 1000
	#peels off as many 1000s (M's) as possible

	if n >= 900:
		ans.append('C')
		ans.append('M')
		n -= 900
	#if 900 or more, we want CM at start

	if n >= 500:
		ans.append('V')
		n-= 500

	if n >= 400:
		ans.append('C')
		ans.append('D')
		n -= 400

	while n >= 100:
		ans.append('C')
		n -= 100

	if n >= 90:
		ans.append('X')
		ans.append('C')
		n -= 90

	if n >= 50:
		ans.append('L')
		n -= 50

	if n >= 40:
		ans.append('X')
		ans.append('L')
		n -= 40

	while n >= 10:
		ans.append('X')
		n -= 10

	if n >= 9:
		ans.append('I')
		ans.append('X')
		n -= 9

	if n >= 5:
		ans.append('V')
		n -= 5

	if n >= 4:
		ans.append('I')
		ans.append('V')
		n -= 4

	while n >= 1:
		ans.append('I')
		n -= 1

	return ans

