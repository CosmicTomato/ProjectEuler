#Exploring Pascal's triangle

#We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:

#However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

#Find the number of entries which are not divisible by 7 in the first one billion (10^9) rows of Pascal's triangle.




#call first row zeroth row
#THEN: convert row number to base seven (e.g. row_num=xyz)
#number of entries not divisible by 7 is equal to product of each digit plus one
#e.g. (x+1)*(y+1)*(z+1)



import convert_int_to_base_x
#convert_int_to_base_x.main( num , x, length ) converts an integer to an arbitrary base number of length equal to 'length' (number must be smaller than x^length)

from math import log



def base_num_to_indivis( base_num ):
#given row number in base number format, returns the number of entries in the row not divisible by base number

	product = 1
	for i in base_num:

		product = product * ( i + 1 )

	return product



def main( base, row ):
#finds number of entries not divisible by base in the first 'row' rows of Pascal's triangle
#as defined, base = 7, row = 10^9

	count = 1
	#to account for row zero (defined as row one in problem)

	int_length = int( log( row ) / ( log( base ) ) ) + 1
	#finds max length of base-'base' number for rows

	for i in range( 1, row ):

		base_num = convert_int_to_base_x.main( i , base , int_length )
		count += base_num_to_indivis( base_num )

	return count









