#imports all primes under one million, then uses them to check if number is prime.
#will only work for numbers <= 10^12
#main function returns 0 if number is not prime, 1 if it is


import import_primes
primes = import_primes.main()


def main( n ):

	if n > ( 10 ** 12 ):
		print( 'error, input for check_prime_fast.main( n ) must be less than or equal to 10^12' )
		return error

	approx_sqrt = int( n ** 0.5 ) + 1
	#gets ceiling of sqrt of number of interest

	i = 0
	while primes[ i ] < approx_sqrt:
		if ( n % primes[ i ] ) == 0:
			return 0
		else:
			i += 1

	return 1
	#i.e. if no prime in list divides number


