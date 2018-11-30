#eul99.py

#PROBLEM STATEMENT
#Largest exponential
#Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
#However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.
#Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
#NOTE: The first two lines in the file represent the numbers in the example given above.


#NOTES:
#need to check a^b > c^d
#same as ln(a^b) > ln(c^d)
#--> b*ln(a) > d*ln(c)
#easy!


#import built-in natural log function
#log(x) = ln(x)
from math import log


def main():

	#imports data from file and puts it in a list
	#each entry is 2 numbers separated by comma, representing exponent (a^b)
	exp_file = open( 'base_exp.txt' )
	holder_list = exp_file.read().split( '\n' )
	exp_file.close()

	#puts all exponent pairs in list (each a^b is listed as [a, b])
	exp_list = []
	for i in range( 0 , len( holder_list ) ):
		exp_list.append( holder_list[ i ].split(',') )
		for j in range( 0 , len( exp_list[ i ] ) ):
			exp_list[ i ][ j ] = int( exp_list[ i ][ j ] )

	#calculates initial value to compare against
	largest_num = exp_list[ 0 ][ 1 ] * log ( exp_list[ 0 ][ 0 ] )
	largest_num_index = 0

	for i in range( 1 , len( exp_list ) ):

		#calculates log of ith exponent
		new_num = exp_list[ i ][ 1 ] * log ( exp_list[ i ][ 0 ] )

		#compares to largest value so far
		#if larger, stores it and its index
		if new_num > largest_num:
			largest_num = new_num
			largest_num_index = i

	#at end we just want the index of the largest exponent (need to add 1 due to the way Python numbers indices)
	return ( largest_num_index + 1 )