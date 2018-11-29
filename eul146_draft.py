#Investigating a Prime Pattern 

#The smallest positive integer n for which the numbers n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, and n^2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

#What is the sum of all such integers n below 150 million?



import MR_primetest
#MR_primetest.main( p ) returns True if number likely prime, False if it is provably not prime.
#works for all p below 3,825,123,056,546,413,051 ( see https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test )


def check_prop( n ):
#checks if n has the desired property. returns True if yes, False if no

#REMOVED
#	if ( base % 4 ) == 1:
#	#additional condition to speed test. see http://mathforum.org/library/drmath/view/62611.html
#REMOVED

	base = n ** 2

#FASTER IN OTHER FNC
#	n_sq = n ** 2
#	if ( n_sq % 3 ) != 1:
#		check = 0
#	#must have n^2=1 (mod 3)
#
#	elif ( n_sq % 5 ) != 0:
#		check = 0
#	#must have n^2=0 (mod 5)
#
#	elif ( n_sq % 7 ) != 2:
#		check = 0
#	#must have n^2=2 (mod 7)
#FASTER IN OTHER FNC

	if MR_primetest.main( base + 1 ):
		if MR_primetest.main( base + 3 ):
			if MR_primetest.main( base + 7 ):
				if MR_primetest.main( base + 9 ):
					if MR_primetest.main( base + 13 ):
						if MR_primetest.main( base + 27 ):
							return True
	return False


def main( max ):
#solves defined problem for n <= max

	ans = 0
	n = 0

	while n <= max:

		n += 10
		#number n must be even. we can also see this from basic reasoning. (n^2+1) must be odd, therefore n even
		#number must also be multiple of 5, thus it must be a multiple of 10

		if ( n % 3 ) != 0:
		#n can't be divisible by 3

			if ( n % 7 ) in [ 3 , 4 ]:
			#must have n^2=2 (mod 7)

				if check_prop( n ):
					ans += n
					print( 'n=' , n )


	return ans


