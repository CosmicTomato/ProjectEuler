#Prime power triples

#The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

#28 = 2^2 + 2^3 + 2^4
#33 = 3^2 + 2^3 + 2^4
#49 = 5^2 + 2^3 + 2^4
#47 = 2^2 + 3^3 + 2^4

#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?




#FAILS BECAUSE IGNORES CHANCE TO DUPLICATE SUMS



import import_primes
primes=import_primes.main()
#gets list of all primes below one million


def main( n ):
#finds how many numbers below n can be expressed as the sum of a prime square, prime cube, and prime fourth power
#in problem as defined, n = 50 * (10**6)

	sum_count = 0
	#will count number of sums

	p_max = ( n - 12 ) ** 0.25
	# -12 is due to min prime being 2

	p_list = []
	for p in primes:
		if p < p_max:
			p_list.append( p )
	#makes list of all primes less than p_max


	for p in p_list:
	#run over every prime less than p_max

		p_rem = n - ( p ** 4 )
		#calcultes remaining amount of n

		q_max = ( p_rem - 4 ) ** ( 1 / 3 )
#NOTE: DOUBTS ABOUT x**(1/3) BEING ACCURATE ENOUGH
#MODIFIED TO (p_rem

		q_list = []
		for q in primes:
			if q < q_max: 
				q_list.append( q )
		#makes list of all primes less than q_max

		for q in q_list:
		#run over every prime less than q_max

			q_rem = p_rem - ( q ** 3 )
			#calcultes remaining amount of n

			r_max = q_rem ** 0.5

			r_list = []
			for r in primes:
				if r < r_max: 
					r_list.append( r )
			#makes list of all primes less than r_max

			sum_count += len( r_list )
			#adds number of primes in r_list to count of viable sums

	return sum_count

