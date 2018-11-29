#Path sum: two ways
#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.


#test_matrix = [ [ 131 , 673 , 234 , 103 , 18 ] , [ 201 , 96 , 342 , 965 , 150 ] , [ 630 , 803 , 746 , 422 , 111 ] , [ 537 , 699 , 497 , 121 , 956 ] , [ 805 , 732 , 524 , 37 , 331 ] ]
#NOTE: problems 82 and 83 are also very similar to this one


def solver( matrix ):
#takes matrix input and finds lowest sum path using described steps

	columns = len( matrix[ 0 ] )
	rows = len( matrix )
	#gets number of rows and columns in matrix

	for i in range( 1 , rows ):
		matrix[ i ][ 0 ] = matrix[ i ][ 0 ] + matrix[ ( i - 1 ) ][ 0 ]
	for j in range( 1 , columns ):
		matrix[ 0 ][ j ] = matrix[ 0 ][ j ] + matrix[ 0 ][ ( j - 1 ) ]
	#gets values to reach leftmost column and top row

	for i in range( 1 , rows ):
		for j in range( 1 , columns ):
			opt_1 = matrix[ ( i - 1 ) ][ j ]
			opt_2 = matrix[ i ][ ( j - 1 ) ]
			matrix[ i ][ j ] = matrix[ i ][ j ] + min( opt_1 , opt_2 )
	#for all remaining entries, in order: look at numbers (sums) above and to the left of the entry. add the small of these two to it.

	return ( matrix[ -1 ][ -1 ] )

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
