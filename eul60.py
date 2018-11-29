#Prime pair sets

#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.




#DOESN'T WORK FOR PROBLEM AS DEFINED ( n = 5 )
#NEED TO BE ABLE TO FIND MULTIPLE OPTIONS FOR STARTING PRIME




import import_primes
primes = import_primes.main()
#pulls all primes below one million

import check_prime
#check_prime.main( n ) returns 0 if n not prime, 1 if n is prime

def main( n ):
#tries to find lowests sum set of n primes which all concatenate pair-wise to form primes

	good_sets = []
	#will store all sets of n primes found

#ARBITRARY SEARCH PARAM
	arb_cap = ( 10 ** 1 )
#ARBITRARY SEARCH PARAM
	for i in range( 1 , arb_cap ):
	#attempts search starting with 3 -> arb_cap-th prime in set. arb_cap is an arbitrary cap set on search

		prime_set = [ primes[ i ] ]
		#starts list with i-th prime (will try to find n-1 more primes fitting criteria)

		j = i
#ARBITRARY SEARCH PARAM
		arb_cap2 = ( 10 ** 4 )
#ARBITRARY SEARCH PARAM
		check = 0
		while j < arb_cap2 and check == 0:
		#there's 78498 primes less than one million, but arb_cap2 puts limit on search

			if len( prime_set ) == n:
				check = 1
			#flips check if set of n primes found

			add_to = 1
			for prime in prime_set:
				if ( check_prime.main( int( str( prime ) + str( primes[ j ] ) ) ) != 1 ) or ( check_prime.main( int( str( primes[ j ] ) + str( prime ) ) ) != 1) :
				#i.e. if either concatentation is not prime
					add_to = 0

			if add_to == 1:
				prime_set.append( primes[ j ] )
			#if primes[j] forms a prime when concatenated with every prime already in list, then add to list

			j += 1
			#increments counter

		if len( prime_set ) == n:
			good_sets.append( prime_set )
		#stores set if set of n primes found

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

