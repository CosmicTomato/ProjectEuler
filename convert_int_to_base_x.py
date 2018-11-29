#converts an integer to an arbitrary base number
#length fixed at length digits (number must be smaller than x^length)
#output is returned as a list of integers of length equal to 'length'

def main( num , x, length ):

	ans = []
	#will hold answer

	i = length - 1
	#labels base index

	while i > 0:

		ans.append( num // ( x ** i ) )
		num = num % (x ** i )
		#finds next digit of num in base x, then calculates remainder

		i -= 1

	ans.append( num )

	return ans

