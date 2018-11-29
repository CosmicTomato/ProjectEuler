#created to solve project euler problem 96
#takes in unfinished sudoku board, outputs answer

#input takes form board = [ [row1 numbers separated by commas], [row2] ... ]
#NOTE: ASSUMES BLANKS ARE MARKED/LISTED AS ZEROES







def pull_solved( board ):
#given a board, creates sets of solved numbers in rows, columns, and squares

	row_sets = [ set(), set(), set(), set(), set(), set(), set(), set(), set() ]
	col_sets = [ set(), set(), set(), set(), set(), set(), set(), set(), set() ]
	square_sets = [ set(), set(), set(), set(), set(), set(), set(), set(), set() ]
	#initializing lists of sets
	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) == 1:
			#i.e. if square already solved

				conj = ( (row_sets[ i ]) | (board[ i ][ j ]) )
				row_sets[ i ] = conj

				conj = ( col_sets[ j ] | board[ i ][ j ] )
				col_sets[ j ] = conj

	#goes through each row and column and pulls solved numbers into a set
	#rest of loop does this for each of the squares, but is a bit more complex
				sq_row = ( i // 3 )
				sq_col = ( j // 3 )
				sq_num = ( sq_row * 3 ) + sq_col
				conj = ( square_sets[ sq_num ] | board[ i ][ j ] )
				square_sets[ sq_num ] = conj

	return ( row_sets, col_sets, square_sets )




def solver_iteration( board ):
#takes in board and gets lists of all solved entries, then tries to reduce list of possibilities in all unsolved squares
#executes 'only choice' and 'single possibility' rules as defined on http://www.sudokudragon.com/sudokustrategy.htm


	( row_sets, col_sets, square_sets ) = pull_solved( board )

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) != 1:
			#i.e. if number is so-far unsolved

				#i is row number, j is column number
				sq_row = ( i // 3 )
				sq_col = ( j // 3 )
				sq_num = ( sq_row * 3 ) + sq_col

				conj = ( ( row_sets[ i ] ) | ( col_sets [ j ] ) | ( square_sets[ sq_num ] ) )
				row_col_sq_set = conj

				for k in row_col_sq_set:
					if k in ( board[ i ][ j ] ):
					#added conditional to prevent errors

						(board[ i ][ j ]).remove( k )
				#removes all solved numbers in row, column, and square from list of possibilities for space

	return board




def solver_iteration_2( board ):
#takes in board and looks at each unsolved entry. sees if it is the only one in it's row/column/square that can be one of the unsolved numbers (in the row/column/square)
#executes 'only square' rule as defined on http://www.sudokudragon.com/sudokustrategy.htm

	( row_sets, col_sets, square_sets ) = pull_solved( board )

	row_lists = [ [], [], [], [], [], [], [], [], [] ]
	col_lists = [ [], [], [], [], [], [], [], [], [] ]
	square_lists = [ [], [], [], [], [], [], [], [], [] ]
	#initializing lists of lists
	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) != 1:
			#i.e. if square NOT already solved

				for k in ( board[ i ][ j ] ):

					row_lists[ i ].append( k )
					col_lists[ j ].append( k )
		#goes through each row and column and pulls solved numbers into a set
		#rest of loop does this for each of the squares, but is a bit more complex
					sq_row = ( i // 3 )
					sq_col = ( j // 3 )
					sq_num = ( sq_row * 3 ) + sq_col
					square_lists[ sq_num ].append( k )

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) != 1:
			#i.e. if square NOT already solved

				#i is row number, j is column number
				sq_row = ( i // 3 )
				sq_col = ( j // 3 )
				sq_num = ( sq_row * 3 ) + sq_col

				changed = 0

				for k in board[ i ][ j ]:
					if ( row_lists[ i ].count( k ) == 1 and k not in row_sets[ i ] ) or ( col_lists[ j ].count( k ) == 1 and k not in col_sets[ j ] ) or ( square_lists[ sq_num ].count( k ) == 1 and k not in square_sets[ sq_num ] ):
					#i.e. if the number is the only unsolved number in its row/column/square that can be that number
					#then it must be that number. and change it to it

						if changed == 0:
						#keeps track of if number has changed already
							board[ i ][ j ] = { k }
							changed = 1

	return board





def solver_iteration_3( board ):
#takes in board, looks for sub-group exclusions to eliminate possiblities in unsolved entries
#see http://www.sudokudragon.com/sudokustrategy.htm

	( row_sets, col_sets, square_sets ) = pull_solved( board )


#WRITTEN JUST FOR ROWS
#TEST
#	print('board=',board)
#TEST
	for i in range( 0 , 9 ):
	#done for each row
		for sect_num in range( 0 , 3 ):
		#done for the 3 sub-sections (each of 3 row entries) in the row

			section_unsolved = []
			rest_of_row_unsolved = []

			for j in range( 0 , 9 ):
			#labels column number

				if len( board[ i ][ j ] ) != 1:
				#i.e. if square NOT already solved

					if j in range( (sect_num * 3) , (sect_num * 3 + 3) ):
						for number in ( board[ i ][ j ] ):
							section_unsolved.append( number )
					else:
						for number in ( board[ i ][ j ] ):
							rest_of_row_unsolved.append( number )
				#puts unsolved numbers from subsection of row into list, other unsolved numbers from rest of row into another list

			for char in range( 1 , 10 ):
			#searches through possible numbers (1 to 9)

				if char not in row_sets[ i ]:
				#i.e. if number 'char' is unsolved in the row

					if ( char in section_unsolved ) and ( char not in rest_of_row_unsolved ):
					#i.e. if unsolved number 'char' can only be in a specific sub-section of the row, then we want to delete it from the other rows in the square that contains the row sub-section


	#TEST
	#					print('section_unsolved=',section_unsolved)
	#					print('rest_of_row_unsolved=',rest_of_row_unsolved)
	#					print('char=',char)
	#TEST

						sq_row = ( i // 3 )

						for m in range( sq_row * 3 , sq_row * 3 + 3):
							for n in range( sect_num * 3 , sect_num * 3 + 3 ):
						#m,n label rows and columns of square of interest

								if m != i:
								#don't want to remove entries from row of interest in square
									if char in board[ m ][ n ] and ( len( board[ m ][ n ] ) !=  1 ):
										board[ m ][ n ].remove( char )
						#remove char from other entries in square (those not in the row being examined)

	return board




def main( board , max_iter ):
#takes in sudoku board and returns answer if it can be found
#will do max_iter iterations before giving up

#TEST
#	board = [ [0,0,3,0,2,0,6,0,0], [9,0,0,3,0,5,0,0,1], [0,0,1,8,0,6,4,0,0], [0,0,8,1,0,2,9,0,0], [7,0,0,0,0,0,0,0,8], [0,0,6,7,0,8,2,0,0], [0,0,2,6,0,9,5,0,0], [8,0,0,2,0,3,0,0,9], [0,0,5,0,1,0,3,0,0] ]
#TEST
#very hard board: [[0, 0, 0, 0, 0, 3, 0, 1, 7], [0, 1, 5, 0, 0, 9, 0, 0, 8], [0, 6, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 7, 0, 0, 0], [0, 0, 9, 0, 0, 0, 2, 0, 0], [0, 0, 0, 5, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0, 0, 2, 0], [5, 0, 0, 6, 0, 0, 3, 4, 0], [3, 4, 0, 2, 0, 0, 0, 0, 0]]

	for row in board:
		for i in range( 0 , 9 ):
			if row[ i ] == 0:
				row[ i ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
	#changes all zeroes into a list of all possible number
			else:
				row[ i ] = set( [ row[ i ] ] )
	#changes all other entries into length-one sets

#	last_solved = 0

	iter = 0
	while iter < max_iter:
		iter += 1

		old_board = board
		board = solver_iteration( old_board )

		old_board = board
		board = solver_iteration_2( old_board )

		old_board = board
		board = solver_iteration_3( old_board )

		solved_count = 0

		for i in range( 0 , 9 ):
			for j in range( 0 , 9 ):
				if len( board[ i ][ j ] ) == 1:
				#i.e. if square already solved

					solved_count += 1

		if solved_count == 81:
		#i.e. if every square solved

			return board

#TEST
#		if solved_count == last_solved:
#			board = solver_iteration_3( board )
#TEST

#		last_solved = solved_count

	print('Error: not enough iterations to solve, or solver will never converge on answer')
	return board






