#Digit factorial chains
#The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

#1! + 4! + 5! = 1 + 24 + 120 = 145

#Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

#169 → 363601 → 1454 → 169
#871 → 45361 → 871
#872 → 45362 → 872

#It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

#69 → 363600 → 1454 → 169 → 363601 (→ 1454)
#78 → 45360 → 871 → 45361 (→ 871)
#540 → 145 (→ 145)

#Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

#How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?







import factorial
#factorial.main(x) returns the factorial of x


def fact_digit_sum(x):
#splits x into its digits and sums their factorials

	sum = 0

	for i in str(x):

		sum += factorial.main( int( i ) )

	return sum





def fact_cycle_len(q):
#finds length of factorial cycle starting with q

	fact_list = [q]

	x = fact_digit_sum( fact_list[-1] )
	#calculates factorial digit sum of last entry in list

	check = 0
	#used to keep loop running until cycle found

	while check == 0:

		if x in fact_list:
		#if x is already in the fact_list (i.e. if x is a repeat), then:

			#del fact_list[ 0 : fact_list.index(x) ]
			#remove entries before the first instance of the repeating number
			#REMOVED SINCE INCORRECT SINCE THIS IS NOT HOW THEY DEFINE CYCLE LENGTH

			#fact_list.append(x)
			#adds x to end of list
			#REMOVED SINCE INCORRECT SINCE THIS IS NOT HOW THEY DEFINE CYCLE LENGTH

			cycle_length = len( fact_list )
			#calculates length of repeating cycle

			#print(fact_list)
			#TEST

			return cycle_length

		else:

			fact_list.append(x)
			#adds x to end of list

		x = fact_digit_sum( fact_list[-1] )
		#calculates new x (factorial digit sum of last entry in list)




def main(below,terms):
#returns number of cycles with exactly (terms) non-repeating terms for starting numbers below (below)

	num = 0
	#counts number of cycles with exactly desired number of terms

	for i in range(1,below):

		#print(i)
		#TEST

		if fact_cycle_len(i) == terms:
		#adds one to num if the factorial cyce length is the exact desired length

			num += 1

	return num


