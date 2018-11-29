#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?




import find_primes_below
primes_list = find_primes_below.main(10**6)     #gets list of all primes below 10^6

import circular_rotations                      #circular_rotations.main(x) returns a list of all permutations of x


circular_primes=[]


for i in primes_list:

	rotations = circular_rotations.main(i)		#gets circular_rotations of i

	prime_permutations = 1				#to be used for a check later

	for j in rotations:				#checks if all of the permutations are in the list of primes

		if prime_permutations == 1:		#works to stop checking once one non-prime has been found

			if j not in primes_list:	#loop switches check to 0 if any non-prime permutation is found

				prime_permutations = 0

	if prime_permutations == 1:			#checks that all permutations are prime

		circular_primes.append(i)		#adds i to list of circular primes

print(circular_primes)
print(len(circular_primes))


