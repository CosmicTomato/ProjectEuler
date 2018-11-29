#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

#If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

#It can be seen that there are 21 elements in this set.

#How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?




#FAILED SECTION - TOO SLOW

	#import find_primes_below
	#find_primes_below.main(x) returns a list of all primes below x
	#primes_list = find_primes_below.main(d)

	#import factor_given_primes
	#factor given primes.main(number,prime_list) returns list of prime factors of number


	#factors_list = [0,1]
	#will hold the prime factors for number 1 - d, "zeroth" entry as placeholder

	#for i in range( 2, (d + 1) ):
	#loop factors numbers 1 - d

		#factors_list.append( factor_given_primes.main( i, primes_list ) )

	#return factors_list
#FAILED SECTION - TOO SLOW

#FAILED SECTION 2 - ALSO TOO SLOW
#	frac_list=[]
#
#	for i in range (2,d+1):
#	#searches through denominators
#
#		for j in range(1,i):
#		#searches through numerators 1 -> i-1
#
#			#if i/j not in frac_list:
#			#adds any new entries to the fraction list
#			#seems slow
#
#				#frac_list.append(i/j)
#
#			frac_list.append(i/j)
#
#	frac_list = list( set( frac_list) )
#	#deletes duplicates
#
#	return frac_list
#FAILED SECTION 2 - ALSO TOO SLOW


#STILL TOO SLOW
def main(d):
#solves defined problem for d = d

	desired = d - 1
	#will count number of fractions, initialized with number of fractions with numerator 1

	import find_primes_below
	#find_primes_below.main(x) returns a list of all primes below x

	primes_list = find_primes_below.main(d)
	#finds all primes below d

	import factor_given_primes
	#factor given primes.main(number,prime_list) returns list of prime factors of number

	for num in range( 2, d ):
	#want to search through numerators from 2 to d-1

		num_factors = list( set( factor_given_primes.main( num, primes_list ) ) )
		#finds prime factors of numerator -- list/set part removes duplicates

		for denom in range( num + 1, d + 1 ):
		#want denominators from one greater than numerator to d

			index = 0
			#used to track index while searching through prime factors

			des_increase = 1
			#will flip to zero if denominator is divisible by any factors of numerator

			len_fact = len( num_factors )
			#finds number of factors of numerator (top index for divisibility search)

			while des_increase == 1 and index < len_fact:
			#continues until a divisor is found or all factors of numerator have been searched through

				if denom % num_factors[ index ] == 0:
				#flips check number if prime factor of numerator evenly divides denominator

					des_increase = 0

				index += 1
				#increments factor index by 1

			desired += des_increase
			#adds des_increase to count of fractions (1 if unique, 0 if not, i.e. denom and numerator share at least 1 prime factor)

	return desired




