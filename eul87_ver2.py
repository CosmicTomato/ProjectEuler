#Prime power triples

#The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

#28 = 2^2 + 2^3 + 2^4
#33 = 3^2 + 2^3 + 2^4
#49 = 5^2 + 2^3 + 2^4
#47 = 2^2 + 3^3 + 2^4

#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?






import import_primes
prime_list = import_primes.main()
#gets list of all primes below one million

#TRUNCATES LIST, SINCE FIRST THOUSAND PRIMES GO PAST sqrt(50,000,000)
prime_list = prime_list[0:1001]
#NEED TO MODIFY IF n>50 million


def main( n ):
#finds how many numbers below n can be expressed as the sum of a prime square, prime cube, and prime fourth power
#in problem as defined, n = 50 * (10**6)

	sum_list = []

	p_max = int( n ** 0.5 )
	q_max = int( n ** ( 1 / 3 ) )
	r_max = int( n ** 0.25 )
	#finds max p, q, r for p^2<n, q^3<n, r^4<n

	for p in prime_list:

		if p <= p_max:

			for q in prime_list:

				if q <= q_max:

					for r in prime_list:

						if r <= r_max:

							pqr_sum = ( p ** 2 ) + ( q ** 3 ) + ( r ** 4 )

							if pqr_sum < n:

								sum_list.append( pqr_sum )

	sum_set = set( sum_list )
	#gets rid of duplicate sums

	return len( sum_set )
















