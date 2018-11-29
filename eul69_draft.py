#Totient maximum

#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

#n	Relatively Prime	φ(n)	n/φ(n)
#2	1	1	2
#3	1,2	2	1.5
#4	1,3	2	2
#5	1,2,3,4	4	1.25
#6	1,5	2	3
#7	1,2,3,4,5,6	6	1.1666...
#8	1,3,5,7	4	2
#9	1,2,4,5,7,8	6	1.5
#10	1,3,7,9	4	2.5
#It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

#Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.



import import_primes
#import_primes.main() pulls all primes less than one million

import factor_given_primes
#factor_given_primes.main( x, primes ) returns a list of all prime factors of x

def factor_below( x ):
#finds prime factors of all numbers from 1 to x

	primes = import_primes.main()

	factor_list = [0,1]
	#zeroth and first entries are placeholders, after that i-th entry will hold factors of i

	for i in range( 2, x + 1 ):
	#factors i and adds a set (unqiue entries) of its factors to the factor_list

		factor_list.append( set( factor_given_primes.main( i, primes ) ) )

#TEST
		print( i )
#TEST


	return factor_list


def find_totients(x):
#finds Euler's totient values for numbers up to x

	#block gets all factors (as sets) for numbers 1 to one million (factors for 0 and 1 are listed as 0 and 1, respectively) -- factors[x] = set of factors of x
	f = open('prime_factors_below_one_million.txt')
	factors = eval( f.read() )
	f.close()
	#end block

	totients = [0,0]
	#will store all totient numbers, first two entries are placeholders for 1 and 2

	for i in range( 2, x + 1 ):
	#will find totient for i

		divisors = factors [ i ]
		#pulls i's list of divisors

		i_tot = 1
		#stores totient of i. starts at 1 since 1 is relatively prime to all numbers

		for j in range( 2, i ):
		#want to look at all numbers 2 through (i-1) to determine if they are relatively prime to i

			if ( divisors & factors[ j ] ) == set():
			#adds one to totient number if i and j are relatively prime (i.e. share no prime factors)

				i_tot += 1

		totients.append(i_tot)
		#adds i's totient to list

	return totients


def main( x ):
#finds number n (<= x) for which ( n / (euler's totient of n) ) is at a maximum

	totients = find_totients(x)
	#gets totients of numbers through x

	max_num = [0 , 0]

	for i in range( 2, len(totients) ):
	#looks at each number up to x, replaces max_num only if i/totient(i) is greater than previous maximum

		if ( i / totients[ i ]) > max_num[0]:

			max_num = [ ( i / totients[ i ] ), i ]

	return max_num



