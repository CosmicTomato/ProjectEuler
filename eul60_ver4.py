#Prime pair sets

#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.





import MR_primetest
#MR_primetest.main( n ) returns True if n is likely prime, False if it is provably not prime
#works for all n below 2,152,302,898,747 according to wikipedia


def check_concat( prime_1, prime_2 ):
#returns True if the 2 primes concatenate together both ways to form a new prime, false otherwise

	concat_1 = int( str( prime_1 ) + str( prime_2 ) )
	if MR_primetest.main( concat_1 ):
		concat_2 = int( str( prime_2 ) + str( prime_1 ) )
		if MR_primetest.main( concat_2 ):
			return True
	return False


def main( prime_cap ):
#tries to find lowests sum set of 5 primes which all concatenate pair-wise to form primes
#only searches for primes below prime_cap

	import import_primes
	primes = import_primes.main()
	#pulls all primes below one million

	if prime_cap > ( 10 ** 6 ):
		print('error, prime_cap > 10**6')

	i = 0
	while primes[ i ] < prime_cap and i < ( len( primes ) - 1 ):
		i += 1
	primes = primes[ 0 : i ]
	#removes all primes above prime_cap from list of primes

	good_sets = []
	#will store all sets of primes found

	for a in primes:
		for b in primes:
			if b > a:
				if check_concat( b , a ):
					for c in primes:
						if c > b:
							if check_concat( c , a ) and check_concat( c , b ):
								for d in primes:
									if d > c:
										if check_concat( d , a ) and check_concat( d , b ) and check_concat( d , c ):
											for e in primes:
												if e > d:
													if check_concat( e , a ) and check_concat( e , b ) and check_concat( e , c ) and check_concat( e , d ):
														good_sets.append( [ a , b , c , d , e ] )

#TEST
	print('good_sets=',good_sets)
#TEST


	min_sum = sum( good_sets[ 0 ] )
	stored_set = good_sets[ 0 ]
	for good_set in good_sets:
		if sum( good_set ) < min_sum:
			min_sum = sum( good_set )
			stored_set = good_set

	return ( stored_set , min_sum )

