#finds pythagorean triples (see https://en.wikipedia.org/wiki/Pythagorean_triple)


import gcd
#gcd.main(a,b) returns the greatest common divisor of a and b. if gcd(a,b)=1, then they are coprime



def main(x):
#finds all primitive pythagorean triples of sum < x
#based on Euclid's formula as explained on https://en.wikipedia.org/wiki/Pythagorean_triple


	trip_list = []
	m = 1
	n = 1

	while ( 2 * ( m ** 2 ) + 2 * m * n ) < x:
	#sum of a,b,c to be generated

		m += 1
		#increments m

		n_max = min( m , ( ( x -  ( 2 * ( m ** 2 ) ) ) // ( 2 * m ) + 1 ) )
		#finds cap for search of n to keep total length below x

#REPLACED
#		n_max = m
#REPLACED

		for n in range( 1 , n_max ):
		#search through n < n_max

			if ( ( m % 2 == 1 ) or ( n % 2 == 1 ) ) and ( ( m % 2 == 0 ) or ( n % 2 == 0 ) ):
			#must have one even and one odd to get primitive triple

				if gcd.main( m , n ) == 1:
				#need m,n to be coprime to get primitive triple

					a = ( ( m ** 2 ) - ( n ** 2 ) )

					b = ( 2 * m * n )

					c = ( ( m ** 2 ) + ( n ** 2 ) )
					#calculates the triple

					trip_list.append( [ a , b , c ] )
					#adds triple to the list

		n = 1
		#needed so while loop doesn't end early

	return trip_list






