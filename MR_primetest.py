#implements simple use case of Miller Rabin primality test
#see: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

#IGNORE THIS
import mod_exp
#mod_exp.main( x , exp , base ) calculates ( x ** exp ) mod base
#IGNORE THIS - mod_exp IS CRAP
#use built in function pow - pow( x , exp , base ) INSTEAD

def main( n ):
#returns False if n provably not prime
#returns True if n is PROBABLY prime

	if ( n % 2 ) == 0:
		return False
	#return false if n even

	ones = [ 1 , ( n - 1 ) ]
	#stores numbers 1 and n-1 to check against

	primes = [ 2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 ]
	#2,3,5,7,11 should work for all n below 2,152,302,898,747 (according to wikipedia)
	#2,3,5,7,11,13,17,19,23 should work for all n below 3,825,123,056,546,413,051 (according to wikipedia)
	#just uses a few primes for 'a' as defined in wikipedia page

	if n in primes:
		return True
	#otherwise can break for primes in list
	
	s = 0
	d = n - 1
	while ( d % 2 ) == 0:
		d = ( d // 2 )
		s += 1
	#pulls as many factors of 2 as possible out of (n-1)

	for a in primes:
		check = False
		r = 0
		while r < s:
		#want to check r from 0 to s
			test_num = pow( a , ( 2 ** r ) * d , n )
			if ( test_num == 1 ) or ( test_num == ( n - 1 ) ):
				check = True
				r = s
			r += 1
		if ( not check ):
			return False
		#check a**d mod n or a**(2**r)*d mod n equals 1 or -1
		#if not then number is confidently not prime

	return True
	#if no failure yet then number is likely prime

