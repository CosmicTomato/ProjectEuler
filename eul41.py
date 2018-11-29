#Pandigital prime

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?






#STRATEGY:
#find all pandigital numbers
#order them from largest to smallest
#start testing if prime, stop once a prime is found



import number_permutations
#number_permutations.main(x) finds all the permutations of the digits of x

import check_prime
#check_prime.main(x) checks if a number is prime and returns 1 if it is (and 0 if it isn't)


def main(x):

	pandigitals = number_permutations.main(x)
	#gets all permutations of entered digits

	pandigitals = sorted(pandigitals)
	#sorts the pandigital permutations (smallest to largest)

	pandigitals = pandigitals [::-1]
	#reverses the order so the pandigitals are largest to smallest

	prime = 0
	#will store eventual answer

	index = 0
	#placeholder index

	while prime == 0:
	#continues until a prime is found

		print(index)

		if check_prime.main( pandigitals[ index ] ) == 1:
		#checks if number is prime

			prime = pandigitals[ index ]
			#stores prime if found

		else:
		#if number checked is not prime, increments index for search

			index += 1

	return prime

