#Prime square remainders

#Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)^n + (pn+1)^n is divided by pn^2.

#For example, when n = 3, p3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.

#The least value of n for which the remainder first exceeds 10^9 is 7037.

#Find the least value of n for which the remainder first exceeds 10^10.


import import_primes
primes = import_primes.main()
#gets list of all primes below 1 million


def main( x ):
#finds least value for n where remainder exceeds x (in problem as defined, x = 10^10)

	i = 1
	#prime index
	p=2
	#first prime
	rem = 1
	#first remainder

	while rem < x:
		i += 1
		p = primes[ (i - 1) ]
		#pulls prime from list
		rem = ( ( ( p - 1 ) ** i ) + ( ( p + 1 ) ** i ) ) % ( p ** 2 )

	return ( p , i , rem )

