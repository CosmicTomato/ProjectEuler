#calculates Euler's totient of a number
#see wikipedia: (https://en.wikipedia.org/wiki/Euler's_totient_function)

import gcd
#gcd.main( a, b ) returns the greatest common divisor of a and b

def main( x ):

	count = 1
	#since 1 will always be relatively prime to an integer

	for i in range( 2, x ):
	#checks all integers >= 2 and less than x. if gcd(x,i) is one (i.e. if i and x are coprime), then increments count

		if gcd.main( x, i ) == 1:

			count += 1

	return count

