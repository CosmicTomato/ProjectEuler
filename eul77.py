#Prime summations

#It is possible to write ten as the sum of primes in exactly five different ways:

#7 + 3
#5 + 5
#5 + 3 + 2
#3 + 3 + 2 + 2
#2 + 2 + 2 + 2 + 2

#What is the first value which can be written as the sum of primes in over five thousand different ways?



import import_primes
primes_list = import_primes.main()
#fetches list of all primes below one million

import copy
#for use later



#COPIED BELOW FROM partition_function.py
#WITH MINOR CHANGES ADDED

#see: https://en.wikipedia.org/wiki/Partition_(number_theory)

#NOTE: ASSUMES INPUT OF 7 OR GREATER

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

#	summation[ -1 ] = ( x // product_list[ -1 ] )
#removed since uncessary and causes errors

	i = len( product_list )

	while i > 0:
	#steps down i and keeps adding in new factors

		i -= 1
		#reduces i by 1

		remainder = rem( x, summation, product_list )
		#find remainder. if zero, stop, otherwise add max number of next biggest factor

		if remainder == 0:

			return (summation, product_list)

		if remainder == 1:
		#search has failed so far. need to backtrack and reduce previous number, then start searching forwards again

			check = 0
			while check == 0:
				if summation[ i ] != 0:
					summation[ i ] -= 1
					check = 1
				else:
					i += 1

		else:
			summation[i] = ( remainder // product_list[i] )

		if i == 0:
			
			return (summation, product_list)

	return (summation, product_list)






def find_next_sum( x, summation, product_list ):
#takes a given sum and finds next one in series

	i = 1
	check = 0

	while check == 0:
	#loop finds smallest factor of sum that is greater than or equal to 2, then reduces number of that factor in sum by 1

		if summation[ i ] == 0:
			i += 1

#NEED TO ADD???		elif i > len(

		else:
			if i == 1:
			#i.e. if pulling out a 3
				if summation[ i ] == 1:
				#cannot pull out a single 3
					i += 1
				else:
					summation[ i ] -= 2
					check = 1
				#must pull out 2 threes
			else:
				summation[ i ] -= 1
				check = 1

	for j in range( 0, i ):
	#sets factors in sum < i to zero

		summation[ j ] = 0

#COPIED FROM ABOVE
	while i > 0:
	#steps down i and keeps adding in new factors

		i -= 1
		#reduces i by 1

		remainder = rem( x, summation, product_list )
		#find remainder. if zero, stop, otherwise add max number of next biggest factor

		if remainder == 0:

			return (summation, product_list)

		if remainder == 1:
		#search has failed so far. need to backtrack and reduce previous number, then start searching forwards again

			check = 0
			while check == 0:
				if summation[ i ] != 0:
					summation[ i ] -= 1
					check = 1
				else:
					i += 1

		else:
			summation[i] = ( remainder // product_list[i] )

		if i == 0:
			
			return (summation, product_list)

	return (summation, product_list)
#COPIED FROM ABOVE







def main( x ):

	if x < 7:
		return 'error'

	else:

		summation_base = []
		product_list = []
		for j in range( 0 , ( x ) ):
			if primes_list[ j ] < ( x - 1 ):
			#needed to limit list of primes to size we want
			#by extending both lists within if statement, we assure that they are the same length
				summation_base.append( 0 )
				product_list.append( primes_list[ j ] )
		#creates empty list with x entries
		#n-th entry equals multiple of n-th prime in summation

	sum_num = 0
	#will count number of possible sums

	summation_base.append( 0 )
	product_list.append( 0 )
	summation = copy.deepcopy( summation_base )
	( summation, product_list ) = shorten( x, summation, product_list )
	#cheap way to get first sum


	while len( summation ) > 1:
	#i.e. until only trying to use 2 to add up to number

#TEST
#		print('successful summation=',summation)
#TEST
		sum_num += 1



#WRONG		if ( summation[-1] == 1 ) and ( ( ( summation[1] * 2 ) +  ( summation[-1] * product_list[-1] ) ) == x ):
#REMOVED

		rem = x - ( 1 * product_list[ -1 ] )
		if ( rem % 2 ) == 1:
			#i.e. if rem odd
			rem -= 3
		max_twos = rem // 2

		if summation[ 0 ] == max_twos:

			( summation, product_list ) = shorten( x, summation, product_list )

		else:

			( summation, product_list ) = find_next_sum( x, summation, product_list )

	if ( x % 2 ) == 0:
		sum_num += 1
	#adds one if x is even. assumes x isn't prime since otherwise it will be just one prime sum.

	return sum_num




def proj_eul( n ):
#keeps using main function until number is found with over n sums
#as defined, n = 5000

	x = 7
	sum_num = main( x )
	while sum_num < n:
		x += 1
		sum_num = main( x )
		print('x=',x)
		print('sum_num=',sum_num)
	return x




