#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?




import find_primes_below
primes_list = find_primes_below.main(10000)	#gets list of all primes below 10000 (4 digits or less)


import number_permutations 			#number_permutations.main(x) returns a list of all permutations of x


matches_criteria=[]				#will hold all numbers meeting desired criteria


for i in primes_list:

	#NOT NECESSASRY AND MISSES SOME## if len("".join(set(str(i)))) == 4:	#checks that there are no duplicate digits in i

		permutations = number_permutations.main(i)	#gets permutations of i

		prime_permutations = []				#starts list of permutations that are prime

		for j in permutations:				#loop adds any prime permutations to list

			if j in primes_list:

				prime_permutations.append(j)

		for k in range (1,5000):	#arithmetic difference between primes must be at least in this range

			if (i + k) in prime_permutations and (i + (2*k)) in prime_permutations:	#checks if there is a 3-tuple of primes

				matches_criteria.append([i,i+k,i+2*k])		#adds them to list of tuples matching criteria

print(matches_criteria)



