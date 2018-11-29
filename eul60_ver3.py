#Prime pair sets

#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.








import import_primes
primes = import_primes.main()
#pulls all primes below one million

import check_prime_fast
#check_prime_fast.main( n ) returns 0 if n not prime, 1 if n is prime

import itertools
#to be used to get combinations of entries from lists




def main( n ):
#tries to find lowests sum set of n primes which all concatenate pair-wise to form primes

	good_pairs = []
	#will store all pairs of primes found

#ARBITRARY SEARCH PARAM
	arb_cap = ( 10 ** 1 )
#ARBITRARY SEARCH PARAM
	for i in range( 0 , arb_cap ):
	#attempts search starting with 3 -> arb_cap-th prime in pair. arb_cap is an arbitrary cap set on search

		j = i
#ARBITRARY SEARCH PARAM
		arb_cap2 = ( 10 ** 4 )
#ARBITRARY SEARCH PARAM
		while j < arb_cap2:
		#there's 78498 primes less than one million, but arb_cap2 puts limit on search

			concat_1 = int( str( primes[ i ] ) + str( primes[ j ] ) )
			concat_2 = int( str( primes[ j ] ) + str( primes[ i ] ) )
			if ( check_prime_fast.main( concat_1 ) == 1 ) and ( check_prime_fast.main( concat_2 ) == 1) :
			#i.e. if both concatentations are prime
				good_pairs.append( [ primes[ i ] , primes[ j ] ] )
				#stores all pairs of primes that fit criteria

			j += 1
			#increments counter

#NOTE: with arb_cap = (10**1) and arb_cap2 = (10**4), good_pairs has 

	better_sets = []
#	for i in range( 0 , arb_cap ):
	#i.e. for each set in good_sets

#		for prime in good_sets[ i ][ 1 ]:
#
#
#
#
#
#
#


#TEST
#	print('good_pairs=',good_pairs)
	print('len(good_pairs)=',len(good_pairs))
#TEST

	return 5

#	min_sum = sum( good_sets[ 0 ] )
#	stored_set = good_sets[ 0 ]
#	for good_set in good_sets:
#		if sum( good_set ) < min_sum:
#			min_sum = sum( good_set )
#			stored_set = good_set
#
#	return ( stored_set , min_sum )

