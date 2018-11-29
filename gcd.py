#calculates the greatest common divisor of two numbers
#based on the Euclidean algorithm (see: https://en.wikipedia.org/wiki/Euclidean_algorithm )

def main( a, b ):
#two numbers of interest are a, b

	ab = [ max(a,b), min(a,b) ]
	#sorts the numbers (greatest first)

	while ab[ 0 ] != ab[ 1 ]:
	#loop continues until the two numbers are equal

		rem = ab[ 0 ] % ab[ 1 ]

		if rem == 0:
		#i.e. if the smaller number equally divides the larger number

			return ab[ 1 ]

		ab = [ ab[ 1 ], rem ]

	return ab[ 0 ]

