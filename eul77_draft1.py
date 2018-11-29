#Prime summations

#It is possible to write ten as the sum of primes in exactly five different ways:

#7 + 3
#5 + 5
#5 + 3 + 2
#3 + 3 + 2 + 2
#2 + 2 + 2 + 2 + 2

#What is the first value which can be written as the sum of primes in over five thousand different ways?




#COPIED BELOW FROM partition_function.py
#WITH MINOR CHANGES ADDED

#tries to calculate the partition function p(n) of a number n
#i.e. the number of sums of positive integers that are equal to n
#includes number itself (i.e. includes sum of one number)

#see: https://en.wikipedia.org/wiki/Partition_(number_theory)


import list_prod_sum
#list_prod_sum.main(a,b) takes two lists a multiplies them pairwise. returns the sum.


def rem ( x, a, b ):
#for later use in main function
#x is start, a & b are lists

	return ( x - list_prod_sum.main( a , b ) )



def shorten( x, summation, product_list ):
#shortens both lists and finds next sum using largest possible factors

	summation = summation[ 0 : -1 ]
	product_list = product_list[ 0 : -1 ]
	#clips off end of both lists

	for i in range( 0, len( summation ) ):
		summation[ i ] = 0

	summation[ -1 ] = ( x // product_list[ -1 ] )

	i = product_list[ -1 ]

	while i > 0:
	#steps down i and keeps adding in new factors

		i -= 1
		#reduces i by 1

		remainder = rem( x, summation, product_list )
		#find remainder. if zero, stop, otherwise add max number of next biggest factor

		if remainder == 0:

			return (summation, product_list)

#NEW
		if i == 0:
			
			return (summation, product_list)
#NEW

		else:

#CHANGE i to prime	summation[i] = ( remainder // i )
			summation[i] = ( remainder // product_list[i] )

	return (summation, product_list)


def find_next_sum( x, summation, product_list ):
#takes a given sum and finds next one in series

	i = 2
	check = 0

	while check == 0:
	#loop finds smallest factor of sum that is greater than or equal to 2, then reduces number of that factor in sum by 1

#TEST
#		print('summation=',summation)
#		print('i=',i)
#TEST


		if summation[ i ] == 0:

			i += 1

		else:

			summation[ i ] -= 1
			check = 1

	for j in range( 1, i ):
	#sets factors in sum < i to zero

		summation[ j ] = 0

	while i > 0:
	#steps down i and keeps adding in new factors

		i -= 1
		#reduces i by 1

		remainder = rem( x, summation, product_list )
		#find remainder. if zero, stop, otherwise add max number of next biggest factor

		if remainder == 0:

			return (summation, product_list)

#NEW
		if i == 0:
			
			return (summation, product_list)
#NEW

		else:

			summation[i] = ( remainder // i )

#NEW
import import_primes
primes_list = import_primes.main()
#fetches list of all primes below one million
#NEW

def main( x ):

	if x < 2:

		return 'error'

	else:

		summation_base = []
		product_list = []
		for j in range( 0 , ( x ) ):
			summation_base.append( 0 )
#CHANGE			product_list.append( a )
			if primes_list[ j ] < x:
			#needed to keep from using gigantic primes
				product_list.append( primes_list[ j ] )
#NEW
#		product_list = [0] + primes_list[ 0 : (x-1) ]
#		#makes list starting with 0, then first (x-1) primes
#NEW
		#creates empty list with x entries
		#n-th entry equals multiple of n in summation

	sum_num = 0
	#will count number of possible sums

	summation = summation_base
#NEED TO CHANGE FIRST SUM
	summation[ 1 ] = 1
	summation[ -1 ] = 1
	#makes new list, with first and last entries of 1



#AHHHHHHHH









	while len( summation ) > 2:

#TEST
		print('successful summation=',summation)
#TEST
		sum_num += 1

#CHANGE		if ( summation[-1] == 1 ) and ( ( ( summation[1] * 1 ) +  ( summation[-1] * product_list[-1] ) ) == x ):
#NEW
		if ( summation[-1] == 1 ) and ( ( ( summation[1] * 2 ) +  ( summation[-1] * product_list[-1] ) ) == x ):
		#since first prime number is 2
#NEW
		#i.e. if the sum is made up of just the one of largest number and twos

			( summation, product_list ) = shorten( x, summation, product_list )

		else:

			( summation, product_list ) = find_next_sum( x, summation, product_list )

#CHANGE	sum_num += 2
#NEW
	if ( x % 2 ) == 0:
		sum_num += 1
	#adds one if x is even. assumes x isn't prime since otherwise it will be just one prime sum.
#NEW

	return sum_num


