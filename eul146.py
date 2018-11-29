#Investigating a Prime Pattern 

#The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

#What is the sum of all such integers n below 150 million?



import MR_primetest
#MR_primetest.main( p ) returns True if number likely prime, False if it is provably not prime.
#works for all p below 3,825,123,056,546,413,051 ( see https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test )


def check_prop( n , mod_list ):
#checks if n has the desired property. returns True if yes, False if no

	base = ( n ** 2 )

	mod_len = len( mod_list )

	for i in range( 0 , mod_len ):
		if ( n % mod_list[ i ][ 0 ] ) not in ( mod_list[ i ][ 1 ] ):
			return False
	#uses mod_list (found below) to quickly eliminate possibilities

	if MR_primetest.main( base + 1 ):
		if MR_primetest.main( base + 3 ):

			if MR_primetest.main( base + 5 ):
				return False
			#added for CONSECUTIVE primes requirement

			elif MR_primetest.main( base + 7 ):
					if MR_primetest.main( base + 9 ):

						if MR_primetest.main( base + 11 ):
							return False
						#added for CONSECUTIVE primes requirement

						elif MR_primetest.main( base + 13 ):

								if MR_primetest.main( base + 15 ):
									return False
								elif MR_primetest.main( base + 17 ):
									return False
								elif MR_primetest.main( base + 19 ):
									return False
								elif MR_primetest.main( base + 21 ):
									return False
								elif MR_primetest.main( base + 23 ):
									return False
								elif MR_primetest.main( base + 25 ):
									return False
								#added for CONSECUTIVE primes requirement

								elif MR_primetest.main( base + 27 ):
									return True
	return False


def main( max_n ):
#solves defined problem for n <= max_n

	add_list = [ 1 , 3 , 7 , 9 , 13 , 27 ]
	#list of numbers added to n^2

	max_add = max( add_list )
	mod_list = []

	for modulo in range( 2 , ( max_add + 1 ) ):
		if MR_primetest.main( modulo ):
		#i.e. if modulo is prime

			mod_list.append( [ modulo , [] ] )

			for i in range( 0 , modulo ):
			#n can be anywhere in this list, but want to eliminate possibilities that can't fit the requirements

				poss_red = []
				for j in add_list:
					poss_red.append( ( ( i ** 2 ) + j ) % modulo )
				#gets all the n^2+x numbers possible, reduced by modulo

				if 0 not in poss_red:
					mod_list[ -1 ][ 1 ].append( i )

	ans = 0
	n = 0

	while n <= max_n:

		n += 10
		#number n must be even. we can also see this from basic reasoning. (n^2+1) must be odd, therefore n even
		#number must also be multiple of 5, thus it must be a multiple of 10

		if check_prop( n , mod_list ):
			ans += n
			print( 'n=' , n )


	return ans


