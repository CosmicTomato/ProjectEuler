#Path sum: two ways

#NOTE: This problem is a more challenging version of Problem 81.

#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.



#NOTE: problems 82 and 83 are also very similar to this one
#SOME CODE COPIED FROM eul81.py and eul82.py

#test_matrix = [ [ 131 , 673 , 234 , 103 , 18 ] , [ 201 , 96 , 342 , 965 , 150 ] , [ 630 , 803 , 746 , 422 , 111 ] , [ 537 , 699 , 497 , 121 , 956 ] , [ 805 , 732 , 524 , 37 , 331 ] ]


import copy


def reduce_frontier( frontier , square , size ):
#checks if new square causes any squares in old frontier to be obsolete
#needs to know size of matrix (ASSUMES SQUARE) for edge case
#size = NUMBER OF COLUMNS/ROWS in matrix
#i.e. ( size - 1 ) is max index possible for a square

	square_above = ( ( square[ 0 ] - 1 ) , square[ 1 ] )
	square_left = ( square[ 0 ] , ( square[ 1 ] - 1 ) )
	square_down_left = ( ( square[ 0 ] + 1 ) , ( square[ 1 ] - 1 ) )
	square_up_right = ( ( square[ 0 ] - 1 ) , ( square[ 1 ] + 1 ) )
	#defines indices of various squares in relation to square of interest

	if ( square_above in frontier ) and ( square_up_right in frontier ):
		frontier.remove( square_above )

	if ( square_left in frontier ) and ( square_down_left in frontier ):
		frontier.remove( square_left )

	if square[ 0 ] == size:
	#i.e. if square is on bottom of matrix
		if ( square_left in frontier ):
			frontier.remove( square_left )

	if square[ 1 ] == size:
	#i.e. if square is on right edge of matrix
		if ( square_above in frontier ):
			frontier.remove( square_above )

	return frontier


def solver( matrix ):
#takes matrix input and finds lowest sum path using described steps

	columns = len( matrix[ 0 ] )
	rows = len( matrix )
	#gets number of rows and columns in matrix

	new_matrix = copy.deepcopy( matrix )

	frontier = [ ( 0 , 0 ) ]
	#list that will hold the "frontier", i.e. the possible starting squares to look for paths from
	#this changes as the matrix is reduced and the "shortest path" to more squares is found
	#NOTE: shortest path is not technically accurate term. the number is reduced to the shortest path that would never cross itself. i.e. the lowest sum path that has a possibility of being the best path (since if a path would cross itself it is automatically not the best path)

	for ij_sum in range( 1 , ( rows + columns + 1 ) ):
		for i in range( 1 , ( ij_sum // 2 ) ):
			j = ij_sum - i
#ADD PERFORM ACTION on i,j and j,i

			options = []

#			for ajfoka:
#				options.append( path_sum )

			best_option = min( options )
			matrix[ i ][ j ] = best_option


			frontier.append( ( i , j ) )
			frontier.append( ( j , i ) )
			frontier = reduce_frontier( frontier , ( i , j ) , columns )
			frontier = reduce_frontier( frontier , ( j , i ) , columns )
			#modify frontier list to include new numbers and exclude old ones

		if ij_sum < rows:
			#ADD PERFORM ACTION on 0,ij_sum and ij_sum, 0

		  			options = []

			for edge in frontier:
				#i.e. for each square on edge of discovered frontier
#				option = 5
#				options.append( option )

			best_option = min( options )
			new_matrix[ 0 ][ ij_sum ] = best_option

			matrix[ ij_sum ][ 0 ]
			#as written assumes square matrix

			frontier.append( ( 0 , ij_sum ) )
			frontier.append( ( ij_sum , 0 ) )
			frontier.remove( ( 0 , ( ij_sum - 1 ) ) )
			frontier.remove( ( ( ij_sum - 1 ) , 0 ) )
			#modify frontier list to include new numbers and exclude old ones

#####################
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
#####################

	min_sum = matrix[ -1 ][ -1 ]
	#pulls bottom right number

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
