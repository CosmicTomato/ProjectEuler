#Searching a triangular array for a sub-triangle having minimum-sum

#In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible.

#In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of −42.

#We wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers sk in the range ±219, using a type of random number generator (known as a Linear Congruential Generator) as follows:

#t := 0
#for k = 1 up to k = 500500:
#    t := (615949*t + 797807) modulo 2^20
#    sk := t−2^19

#Thus: s1 = 273519, s2 = −153582, s3 = 450905 etc

#Our triangular array is then formed using the pseudo-random numbers thus:
#s1
#s2  s3
#s4  s5  s6 
#s7  s8  s9  s10
#...

#Sub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements directly below it from the next row, the three elements directly below from the row after that, and so on).
#The "sum of a sub-triangle" is defined as the sum of all the elements it contains.
#Find the smallest possible sub-triangle sum.



import copy


def main():

	orig_tri = [ [ 273519 ] ]
	#triangle will have each row be a separate list of comma-separate values

	t = 797807
	row = 1
	full_row_ind = ( row * ( row + 1 ) ) // 2

	for k in range( 2 , 500501 ):
	#starts with 2 since first number is already in triangle

		t = ( ( 615949 * t )+ 797807 ) % ( 2 ** 20 )
		s = t - ( 2 ** 19 )
		#calculates new t, s

		if k > full_row_ind:
			orig_tri.append( [ s ] )
			row += 1
			full_row_ind = ( row * ( row + 1 ) ) // 2
		#starts new row and calculates index to start next row

		else:
			orig_tri[ ( row - 1 ) ].append( s )

#ORIGINAL TRIANGLE NOW DONE

	min_sum = 0
	for row in range( 0 , len( orig_tri ) ):
		for i in orig_tri[ row ]:
			if ( i < min_sum ):
				min_sum = i
	#finds minimum value in original triangle
	#(will be superseded if better value found)

	new_tri = copy.deepcopy( orig_tri )
	new_tri = new_tri[ 0 : - 1 ]
	#copies original triangle and clips off last row

	for reduce in range( 1 , len( orig_tri ) ):
	#need one less "reduction" of triangle than number of rows
		for row in range( 0 , ( len( orig_tri ) - reduce ) ):
		#operate on all rows of reduced triangle other than the last one
		#(number of rows gets reduced by one each time)

			for i in range( 0 , len( new_tri[ row ] ) ):
				new_tri[ row ][ i ] += sum( orig_tri[ ( row + reduce ) ][ i : ( i + reduce + 1 ) ] )
				#need to sum (reduce+1) entries of row (reduce) rows down from entry of interest

		for row in range( 0 , len( new_tri ) ):
			for i in new_tri[ row ]:
				if ( i < min_sum ):
					min_sum = i
		#checks if any number in new reduced triangle is less than the previous minimum sum

		new_tri = new_tri[ 0 : - 1 ]
		#clips off last row of triangle
#TEST
		print( 'len( new_tri )= ' , len( new_tri ) )
		print( 'min_sum = ' , min_sum )
#TEST


	return min_sum


