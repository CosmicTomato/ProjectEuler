#prime digit replacements

#By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.



#notes
#need to start with 3+ digit prime
#find primes at start, then search through those (probably < 10^6)
#try replacing 1st and 2nd digit, then 1st and 3rd, then 2nd and third...
#i.e. for i in range (0, len (str (prime) ) ): for j in range (i+1, same end) where i and j are indices of digits
#for each replacement:
#start with empty found_primes list
#serach through replacing the different digit sets with 1-9 (both replacements are same digit as defined in problem), and add any primes found to primelist
#if len(primelist) == 8, return primelist
#otherwise move to next prime
#try with example first!



import find_primes_below




def main(x):
#solves defined problem for first prime with x-prime value family

	prime_list = find_primes_below.main( 2 * 10 ** 6 )
	#finds all primes below (10^6) and puts them in a list

	prime_index = 25
	#keeps track of index for prime that is being tried
	#starts with 25 as that is the index of the first 3-digit prime
	#11412

	prime = prime_list[ prime_index ]
	#pulls the prime from the prime list

	prime_str = str ( prime )
	#gets a string of the prime

	number_of_primes = len (prime_list)
	#finds number of primes less than 10^6 (to use as max index cap)

	while prime_index < ( number_of_primes - 1 ):
	#searches until desired result found or all primes exhausted

		prime_length = len( prime_str )
		#finds length of prime

		check_repeats = 0
		for q in range( 0, 10 ):
		#check if any digit repeats in prime, if it does switches check to 1

			if prime_str.count( str( q ) ) >= 2:

				check_repeats = 1

		if check_repeats == 1:
		#loop only executes if prime has at least one digit that repeats

			for i in range( 0, prime_length - 1 ):
			#first replacement digit index

				for j in range(i+1, prime_length ):
				#second replacement digit index

					prime_str = str ( prime )
					#resets prime string for each i,j combination

					if int( prime_str[i] ) == int( prime_str[j] ):
					#only executes if digits match in original prime

#TEST
#						print('i=',i,'j=',j)
#TEST

						found_primes=[]
						#will store any primes found in digit replacements
						#resets list for each i,j combination

						for k in range( 0, 10 ):
						#try replacing digits with 0-9


							prime_l = list ( prime_str )
							#creates a list from prime_str to allow item assignment

							prime_l[i] = str( k )
							prime_l[j] = str( k )
							#replaces the 2 digits i,j of prime_list with k

							prime_str = ''.join(prime_l)
							#converts back to prime_str to get correct formatting with digits replaced

	#TEST
	#TEST						print(prime_str)
	#TEST

	#TEST
	#TEST						print('i=',i,'j=',j,'k=',k)
	#TEST

							if i != 0 or k != 0:
							#prevents leading zeroes

								if int( prime_str ) in prime_list:

									found_primes.append ( prime_str )
									#adds any primes found in digit replacement to found_primes list

	#TEST
						print(found_primes)
	#TEST

						if len( found_primes ) == x:
						#i.e. if prime is part of an x-prime value family

							return found_primes

		prime_index += 1
		prime = prime_list[ prime_index ]
		prime_str = str ( prime )
		#increments prime_index and gets a string of the next prime in prime_list

#TEST
		print('prime=',prime)
#TEST

		check_repeats = 0
		for q in range( 0, 10 ):
		#check if any digit repeats in prime, if it does switches check to 1

			if prime_str.count( str( q ) ) >= 2:

				check_repeats = 1


	return 0
	#returns 0 if search fails





