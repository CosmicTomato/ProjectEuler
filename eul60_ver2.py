#Prime pair sets

#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.








import import_primes
primes = import_primes.main()
#pulls all primes below one million

import check_prime_fast
#check_prime_fast.main( n ) returns 0 if n not prime, 1 if n is prime


import copy



def main( n ):
#tries to find lowests sum set of n primes which all concatenate pair-wise to form primes

	good_sets = []
	#will store all sets of primes found

#ARBITRARY SEARCH PARAM
	arb_cap = ( 10 ** 1 )
#ARBITRARY SEARCH PARAM
	for i in range( 0 , arb_cap ):
	#attempts search starting with 3 -> arb_cap-th prime in pair. arb_cap is an arbitrary cap set on search

		good_sets.append( [ primes[ i ] , [] ] )

		j = i
#ARBITRARY SEARCH PARAM
		arb_cap2 = ( 10 ** 4 )
#ARBITRARY SEARCH PARAM
		check = 0
		while j < arb_cap2:
		#there's 78498 primes less than one million, but arb_cap2 puts limit on search

			concat_1 = int( str( primes[ i ] ) + str( primes[ j ] ) )
			concat_2 = int( str( primes[ j ] ) + str( primes[ i ] ) )
			if ( check_prime_fast.main( concat_1 ) == 1 ) and ( check_prime_fast.main( concat_2 ) == 1) :
			#i.e. if both concatentations are prime
				good_sets[ i ][ 1 ].append( primes[ j ] )
				#stores all primes > prime[i] that can concatenate with prime[i] in good_sets[i][1]

			j += 1
			#increments counter

#NOTE: good_sets now consists of arb_cap entries with first entry of a single prime and 2nd entry of all primes that concatenate with it to make a prime
#e.g. for arb_cap = (10**1) and arb_cap2 = (10**4), good_sets[1] has a length of 1067, indicating 1067 primes can concatenate with 3 to make other primes






#THIS PART TAKES TOO LONG!!!

	better_sets = copy.deepcopy( good_sets )

	for i in range( 0 , arb_cap ):
	#i.e. for each set in good_sets

		if good_sets[ i ][ 1 ] != []:
		#i.e. only perform if at least one prime concatenates with the base prime

			for j in range( 0 , len( good_sets[ i ][ 1 ] ) ) :
			#i.e. for all primes that concatenate with base prime good_sets[ i ][ 0 ]

				better_sets[ i ][ 1 ][ j ] = [ better_sets[ i ][ 1 ][ j ] , [] ]
				#creates list containing previous entry and empty list

				for k in range( ( j + 1 ) , len( good_sets[ i ][ 1 ] ) ):
				#check which primes above it in list concatentate with it to make primes

					concat_3 = int( str( good_sets[ i ][ 1 ][ j ] ) + str( good_sets[ i ][ 1 ][ k ] ) )
					concat_4 = int( str( good_sets[ i ][ 1 ][ k ] ) + str( good_sets[ i ][ 1 ][ j ] ) )
					if ( check_prime_fast.main( concat_3 ) == 1 ) and ( check_prime_fast.main( concat_4 ) == 1) :
						better_sets[ i ][ 1 ][ j ][ 1 ].append( good_sets[ i ][ 1 ][ k ] )

#
#
#
#
#











#TEST
#	print('good_sets=',good_sets)
#	print('len(good_sets)=',len(good_sets))
	print('better_sets=',better_sets)
	print('len(better_sets)=',len(better_sets))
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

