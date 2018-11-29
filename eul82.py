#Path sum: two ways

#NOTE: This problem is a more challenging version of Problem 81.

#The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the left column to the right column.




#NOTE: problems 82 and 83 are also very similar to this one
#SOME CODE COPIED FROM eul81.py

#test_matrix = [ [ 131 , 673 , 234 , 103 , 18 ] , [ 201 , 96 , 342 , 965 , 150 ] , [ 630 , 803 , 746 , 422 , 111 ] , [ 537 , 699 , 497 , 121 , 956 ] , [ 805 , 732 , 524 , 37 , 331 ] ]


import copy



def solver( matrix ):
#takes matrix input and finds lowest sum path using described steps

	columns = len( matrix[ 0 ] )
	rows = len( matrix )
	#gets number of rows and columns in matrix

	new_matrix = copy.deepcopy( matrix )

	for col_num in range( 1 , columns ):
	#performed for each column starting with the 2nd

		for i in range( 0 , rows ):
		#for each entry in column
			options = []
			for j in range( 0 , rows ):
			#for each possible starting space
				option = matrix[ i ][ col_num ] + matrix[ j ][ ( col_num - 1 ) ]
				if j < i:
					for k in range( j , i ):
						option += matrix[ k ][ col_num ]
				elif j > i:
					for k in range( ( i + 1 ) , ( j + 1 ) ):
						option += matrix[ k ][ col_num ]
				options.append( option )
			best_option = min( options )
			new_matrix[ i ][ col_num ] = best_option
		#gets values to reach column from anywhere in previous column

		matrix = copy.deepcopy( new_matrix )
		#transfers new values into matrix

	last_column = []
	for i in range( 0 , rows ):
		last_column.append( matrix[ i ][ -1 ] )
	min_sum = min( last_column )
	#pulls last column of numbers and finds its minimum

	return min_sum

def main():

	a = open( 'matrix.txt' )
	f = list( a.read().split("\n") )
	a.close()
	f = f[ 0 : -1 ]
	matrix = []
	for i in range( 0 , len( f ) ):
		matrix.append( f[ i ].split(',') )
		for j in range( 0 , len( matrix[ i ] ) ):
			matrix[ i ][ j ] = int( matrix[ i ][ j ] )
	#pulls and formats matrix

	ans = solver( matrix )
	return ans
