#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


import find_primes_below	#find_primes_below.main(x) returns a list containing all prime numbers below x

import factor_given_primes	#factor_given_primes.main(number,primes) returns list containing all prime factors of number (including duplicates), or empty list if factoring fails

four_factor_numbers = []

search_end = 1000	#arbitrarily chosen end for search

primes_list = find_primes_below.main(search_end)

desired_set = []	#will hold the numbers we want to find


i = 1
while i < search_end ** 2 and desired_set==[]:		#arbitrarily chosen end for search

	factors_list = 	factor_given_primes.main(i, primes_list)	#gets list of prime factors

	if len(set(factors_list)) == 4:		#checks that number has exactly 4 prime factors

		four_factor_numbers.append(i)	#if it does, adds to list

		if len(four_factor_numbers) >= 4:

			if four_factor_numbers[-2]==four_factor_numbers[-1]-1:			#nested criteria for last 4 numbers to be sequential
				if four_factor_numbers[-3]==four_factor_numbers[-2]-1:
					if four_factor_numbers[-4]==four_factor_numbers[-3]-1:

						desired_set = four_factor_numbers[-4:]		#puts numbers in desired list if condition is met

	i = i + 1

print(four_factor_numbers) ###TEST
print('desired numbers are: ',desired_set)
