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

		else:

			summation[i] = ( remainder // i )

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

		else:

			summation[i] = ( remainder // i )



def main( x ):

	if x < 2:

		return 'error'

	else:

		summation_base = []
		product_list = []
		for j in range( 0 , ( x ) ):
			summation_base.append( 0 )
			product_list.append( j )
		#creates empty list with x entries
		#n-th entry equals multiple of n in summation
		#also creates list with entries 0 to (x-1), to be multiplied product-wise with summation list

	sum_num = 0
	#will count number of possible sums

	summation = summation_base
	summation[ 1 ] = 1
	summation[ -1 ] = 1
	#makes new list, with first and last entries of 1

	while len( summation ) > 2:

#TEST
#		print('successful summation=',summation)
#TEST
		sum_num += 1

		if ( summation[-1] == 1 ) and ( ( ( summation[1] * 1 ) +  ( summation[-1] * product_list[-1] ) ) == x ):
		#i.e. if the sum is made up of just the one of largest number and ones

			( summation, product_list ) = shorten( x, summation, product_list )

		else:

			( summation, product_list ) = find_next_sum( x, summation, product_list )

	sum_num += 2
	#accounts for sum that is all ones, and sum that is just the number itself

	return sum_num


