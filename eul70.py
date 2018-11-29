#Totient permutation
#

#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

#Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

#Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.



#from wikipedia:
#φ(n) = n times product of (1 - 1/p) where p are the prime factors of n
#thus, search for max of product of (1 - 1/p) to find minimum of n/φ(n)
#this will be  number with large prime factors
#in order for φ(n) to be a permuation of n, n can't have a single prime factor - since φ(n) of a prime = (n-1) which is not going to be a permutation of n
#thus, search for number with 2 large prime factors


import find_primes_below
#find_primes_below.main(x) returns a list of primes below x

import number_permutations
#number_permutations.main(x) returns a list of all permutations of the digits of x (including x itself)

def totient_over_n(p_list):
#finds the value of the product of (1-1/p) for a list of prime factors (p_list)

	ans = 1

	for p in p_list:
	#multiplies each step of product

		ans = ans * ( 1 - (1 / p) )

	return ans

def main():
#solves defined problem by searching through pairs of primes

	primes = find_primes_below.main( 10**4 )
	#arbitrarily chosen cap for primes based on problem cap of 10^7

	stored_num = [ 0, 0 ]
	#will store highest totient / n as well as the number n

	for i in primes:

		for j in primes:

			n = i * j
			#since we are searching for numbers with 2 prime factors

			if n < (10 ** 7):
			#requirement for max n

				p_list = [ i, j ]
				tot_div_n = totient_over_n( p_list )
				#calculates totient/n using above function

				totient = tot_div_n * n
				#calculates the totient

				if totient in number_permutations.main( n ):
				#i.e. if φ(n) is a permutation of n

					if tot_div_n > stored_num[ 0 ]:
					#i.e. if higher than last previous highest totient/n found

						stored_num = [ tot_div_n, n ]
						#stores numbers to be compared to or for answer if best

#TEST
						print('i=',i,'j=',j,'stored_num=',stored_num)
#TEST

	return stored_num



