#Path sum: two ways

#NOTE: This problem is a more challenging version of Problem 81.

#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down.



#NOTE: problems 82 and 83 are also very similar to this one
#SOME CODE COPIED FROM eul81.py and eul82.py

#test_matrix = [ [ 131 , 673 , 234 , 103 , 18 ] , [ 201 , 96 , 342 , 965 , 150 ] , [ 630 , 803 , 746 , 422 , 111 ] , [ 537 , 699 , 497 , 121 , 956 ] , [ 805 , 732 , 524 , 37 , 331 ] ]


import copy


def solver_iter( orig_matrix , current_matrix , frontier ):
#takes in original matrix, current matrix state, and list of square indices that changes in last iteration

	columns = len( orig_matrix[ 0 ] )
	rows = len( orig_matrix )
	#gets number of rows and columns in matrix

	new_frontier = []

	for edge in frontier:
		ind_up = ( ( edge[ 0 ] - 1 ) , ( edge[ 1 ] ) )
		ind_dn = ( ( edge[ 0 ] + 1 ) , ( edge[ 1 ] ) )
		ind_lft = ( ( edge[ 0 ] ) , ( edge[ 1 ] - 1 ) )
		ind_rt = ( ( edge[ 0 ] ) , ( edge[ 1 ] + 1 ) )
		adj_list = [ ind_up , ind_dn , ind_lft , ind_rt ]
		#gets indices of 4 squares surrounding edge square

		edge_val = current_matrix[ edge[ 0 ] ][ edge[ 1 ] ]
		#pulls value of edge square

		for adj_sq in adj_list:
			if ( adj_sq[ 0 ] >= 0 ) and ( adj_sq[ 0 ] < rows ) and ( adj_sq[ 1 ] >= 0 ) and ( adj_sq[ 1 ] < columns ):
			#i.e. if square is inside of matrix
				if ( current_matrix[ adj_sq[ 0 ] ][ adj_sq[ 1 ] ] == orig_matrix[ adj_sq[ 0 ] ][ adj_sq[ 1 ] ] ):
				#i.e. if path sum has not yet been found for square, put in the first sum found
					current_matrix[ adj_sq[ 0 ] ][ adj_sq[ 1 ] ] = ( edge_val + ( orig_matrix[ adj_sq[ 0 ] ][ adj_sq[ 1 ] ] ) )
					new_frontier.append( ( adj_sq[ 0 ] , adj_sq[ 1 ] ) )

				elif ( edge_val + ( orig_matrix[ adj_sq[ 0 ] ][ adj_sq[ 1 ] ] ) ) < ( current_matrix[ adj_sq[ 0 ] ][ adj_sq[ 1 ] ] ):
				#i.e. if edge + original sq value is less than the best value found yet for the square ( the value in the current matrix )
					current_matrix[ adj_sq[ 0 ] ][ adj_sq[ 1 ] ] = ( edge_val + ( orig_matrix[ adj_sq[ 0 ] ][ adj_sq[ 1 ] ] ) )
					new_frontier.append( ( adj_sq[ 0 ] , adj_sq[ 1 ] ) )
					#if new number is better, stores it and notes that the index has changed by adding it to the frontier list

	return( current_matrix , new_frontier )


def solver( matrix ):
#takes matrix input and finds lowest sum path using described steps

	orig_matrix = copy.deepcopy( matrix )
	current_matrix = copy.deepcopy( matrix )
	#makes copies of matrix

	frontier = [ ( 0 , 0 ) ]
	#list that will hold the "frontier", i.e. the possible starting squares to look for paths from

	while frontier != []:
	#continues until no more shortest paths can be found
		( current_matrix , frontier ) = solver_iter( orig_matrix , current_matrix , frontier )

	return current_matrix[ -1 ][ -1 ]
	#pulls lower right corner of matrix with shortest paths filled in



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
