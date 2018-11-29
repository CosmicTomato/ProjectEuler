#created to solve project euler problem 96
#takes in unfinished sudoku board, outputs answer

#input takes form board = [ [row1 numbers separated by commas], [row2] ... ]
#NOTE: ASSUMES BLANKS ARE MARKED/LISTED AS ZEROES







def pull_sets( board ):
#given a board, creates sets of solved and unsolved numbers in rows, columns, and squares
#first entry in row_sets[ n ] is the solved numbers in row n, 2nd entry is the unsolved numbers in row n

	row_sets = [ [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ] ]
	col_sets = [ [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ] ]
	square_sets = [ [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ], [ set() , set() ] ]
	#initializing lists of sets
	#first entry in row_sets[ n ] is the solved numbers in row n, 2nd entry is the unsolved numbers in row n

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) == 1:
			#i.e. if square already solved

				conj = ( row_sets[ i ][ 0 ] | board[ i ][ j ][ 1 ] )
				row_sets[ i ][ 0 ] = conj

				conj = ( col_sets[ j ][ 0 ] | board[ i ][ j ][ 1 ] )
				col_sets[ j ][ 0 ] = conj

	#goes through each row and column and pulls solved numbers into a set
	#rest of loop does this for each of the squares, but is a bit more complex
				sq_row = ( i // 3 )
				sq_col = ( j // 3 )
				sq_num = ( sq_row * 3 ) + sq_col
				conj = ( square_sets[ sq_num ][ 0 ] | board[ i ][ j ][ 1 ] )
				square_sets[ sq_num ][ 0 ] = conj

			else:
			#i.e. if square not already solved
			#does the same thing except for 2nd entries in each part of the row/column/square lists

				conj = ( row_sets[ i ][ 1 ] | board[ i ][ j ][ 1 ] )
				row_sets[ i ][ 1 ] = conj

				conj = ( col_sets[ j ][ 1 ] | board[ i ][ j ][ 1 ] )
				col_sets[ j ][ 1 ] = conj

				sq_row = ( i // 3 )
				sq_col = ( j // 3 )
				sq_num = ( sq_row * 3 ) + sq_col
				conj = ( square_sets[ sq_num ][ 1 ] | board[ i ][ j ][ 1 ] )
				square_sets[ sq_num ][ 1 ] = conj

	return ( row_sets, col_sets, square_sets )


def pull_unsolved_lists( board ):
#goes through each row, column, and square and pulls unsolved numbers into lists
#NOTE: uses zeros for placeholders for solved entries

	row_lists = [ [], [], [], [], [], [], [], [], [] ]
	col_lists = [ [], [], [], [], [], [], [], [], [] ]
	square_lists = [ [], [], [], [], [], [], [], [], [] ]
	#initializing lists of lists
	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
		#goes through each row, column, and square and pulls unsolved numbers into lists
		#NOTE: uses zeros for placeholders for solved entries

			sq_row = ( i // 3 )
			sq_col = ( j // 3 )
			sq_num = ( sq_row * 3 ) + sq_col

			if board[ i ][ j ][ 0 ] == 0:
			#i.e. if entry NOT already solved

				for k in ( board[ i ][ j ][ 1 ] ):
					row_lists[ i ].append( k )
					col_lists[ j ].append( k )
					square_lists[ sq_num ].append( k )

			else:
			#i.e. if entry already solved

				row_lists[ i ].append( 0 )
				col_lists[ j ].append( 0 )
				square_lists[ sq_num ].append( 0 )

	return ( row_lists, col_lists, square_lists )



def remove_from_entry( entry , x ):
#used to modify entries in board by removing x from their list of possibilities. contains logic to prevent errors

	if entry[ 0 ] == 1:
	#i.e. if already solved
		return entry

	elif len( entry[ 1 ] ) == 1:
	#i.e. if entry is now solved
		entry[ 0 ] = 1
		return entry

	elif x in ( entry[ 1 ] ):
		entry[ 0 ].remove( x )
		if len( entry[ 1 ] ) == 1:
		#i.e. if entry is now solved
			entry[ 0 ] = 1
		return entry

	else:
		return entry



def solver_iteration( board ):
#takes in board and gets lists of all solved entries, then tries to reduce list of possibilities in all unsolved squares
#executes 'only choice' and 'single possibility' rules as defined on http://www.sudokudragon.com/sudokustrategy.htm


	( row_sets, col_sets, square_sets ) = pull_sets( board )
	#given a board, creates sets of solved and unsolved numbers in rows, columns, and squares
	#first entry in row_sets[ n ] is the solved numbers in row n, 2nd entry is the unsolved numbers in row n

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if board[ i ][ j ][ 0 ] == 0:
			#i.e. if number is so-far unsolved

				#i is row number, j is column number
				sq_row = ( i // 3 )
				sq_col = ( j // 3 )
				sq_num = ( sq_row * 3 ) + sq_col

				conj = ( ( row_sets[ i ][ 0 ] ) | ( col_sets [ j ][ 0 ] ) | ( square_sets[ sq_num ][ 0 ] ) )
				row_col_sq_set = conj
				#gets set of all solved numbers in row/column/square

				for k in row_col_sq_set:
					if k in ( board[ i ][ j ][ 1 ] ):
					#added conditional to prevent errors

						entry = board[ i ][ j ]
						board[ i ][ j ] = remove_from_entry( entry , k )
				#removes all solved numbers in row, column, and square from list of possibilities for space

	return board




def solver_iteration_2( board ):
#takes in board and looks at each unsolved entry. sees if it is the only one in it's row/column/square that can be one of the unsolved numbers (in the row/column/square)
#executes 'only square' rule as defined on http://www.sudokudragon.com/sudokustrategy.htm

	( row_sets, col_sets, square_sets ) = pull_sets( board )
	#given a board, creates sets of solved and unsolved numbers in rows, columns, and squares
	#first entry in row_sets[ n ] (row_sets[n][0]) is the solved numbers in row n, 2nd entry is the unsolved numbers in row n

	( row_lists, col_lists, square_lists ) = pull_unsolved_lists( board )
	#goes through each row, column, and square and pulls unsolved numbers into lists
	#NOTE: uses zeros for placeholders for solved entries

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if board[ i ][ j ][ 0 ] == 0:
			#i.e. if square NOT already solved

				#i is row number, j is column number
				sq_row = ( i // 3 )
				sq_col = ( j // 3 )
				sq_num = ( sq_row * 3 ) + sq_col

				for k in board[ i ][ j ][ 1 ]:
					if ( k in row_sets[ i ][ 1 ] ) or ( k in col_sets[ j ][ 1 ] ) or ( k in square_sets[ sq_num ][ 1 ] ):
					#i.e. k is indeed unsolved
						if ( row_lists[ i ].count( k ) == 1 ) or ( col_lists[ j ].count( k ) == 1 ) or ( square_lists[ sq_num ].count( k ) == 1 ):
						#i.e. if the number is the only unsolved number in its row/column/square that can be that number
						#then it must be that number. and change it to it

							if board[ i ][ j ][ 0 ] == 0:
							#keeps track of if number has changed already. only runs if number not yet solved
#TEST
	#							print('i=',i,'j=',j)
#TEST

								board[ i ][ j ] = [ 1 , { k } ]

	return board





def solver_iteration_3( board ):
#takes in board, looks for sub-group exclusions to eliminate possiblities in unsolved entries
#see http://www.sudokudragon.com/sudokustrategy.htm

	( row_sets, col_sets, square_sets ) = pull_sets( board )
	#given a board, creates sets of solved and unsolved numbers in rows, columns, and squares
	#first entry in row_sets[ n ] (row_sets[n][0]) is the solved numbers in row n, 2nd entry is the unsolved numbers in row n

	rows_unsolved = []
	for i in range( 0 , 9 ):
		rows_unsolved.append( { 1, 2, 3, 4, 5, 6, 7, 8, 9 } )
		for j in row_sets[ i ]:
			rows_unsolved[ i ].remove( j )
		#gets sets of unsolved numbers in rows

	row_unsolved = [ [], [], [], [], [], [], [], [], [] ]
	col_unsolved = [ [], [], [], [], [], [], [], [], [] ]
	square_unsolved = [ [], [], [], [], [], [], [], [], [] ]

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):

			sq_row = ( i // 3 )
			sq_col = ( j // 3 )
			sq_num = ( sq_row * 3 ) + sq_col

			if len( board[ i ][ j ] ) != 1:
			#i.e. if square NOT already solved

				row_unsolved[ i ].append( board[ i ][ j ] )
				col_unsolved[ j ].append( board[ i ][ j ] )
				square_unsolved[ sq_num ].append( board[ i ][ j ] )

			else:
			#i.e. if square already solved

				row_unsolved[ i ].append( 0 )
				col_unsolved[ j ].append( 0 )
				square_unsolved[ sq_num ].append( 0 )
	#creates lists of all the sets in the unsolved squares. uses zeroes for the solved spaces to keep spacing correct

	for i in range( 1 , 10 ):
	#searches through possible numbers (1 to 9)

#WRITTEN JUST FOR ROWS

		for j in range( 0 , 9 ):
		#done for each row

			des_entries = []
			for entry in row_unsolved[ j ][ 0 : 3 ]:
				if entry != 0:
					for number in entry:
						des_entries.append( number )
			#pulls all numbers in first 3 entries in row_unsolved[ j ] into a list

			undes_entries = []
			for entry in row_unsolved[ j ][ 3 : 9 ]:
				if entry != 0:
					for number in entry:
						undes_entries.append( number )
			#pulls numbers from all other entries in row into a list

			if ( i in des_entries ) and ( i not in undes_entries ):
			#i.e. if number i (1-9) can be in first part of row but not the rest

					sq_row = ( j // 3 )

					for m in range( ( sq_row * 3 ) , ( ( sq_row * 3 ) + 3 ) ):
						for n in range( 0 , 3 ):
							if m != j:
							#don't want to remove entries from row of interest in square
								if i in board[ m ][ n ] and ( len( board[ m ][ n ] ) > 1 ):
									board[ m ][ n ].remove( i )
					#remove i from other entries in square


			des_entries = []
			for entry in row_unsolved[ j ][ 3 : 6 ]:
				if entry != 0:
					for number in entry:
						des_entries.append( number )
			#pulls all numbers in middle 3 entries in row_unsolved[ j ] into a list

			undes_entries = []
			for entry in row_unsolved[ j ][ 0 : 3 ]:
				if entry != 0:
					for number in entry:
						undes_entries.append( number )
			for entry in row_unsolved[ j ][ 6 : 9 ]:
				if entry != 0:
					for number in entry:
						undes_entries.append( number )
			#pulls numbers from all other entries in row into a list

			if ( i in des_entries ) and ( i not in undes_entries ):
			#i.e. if number i (1-9) can be in middle part of row but not the rest

					sq_row = ( j // 3 )

					for m in range( ( sq_row * 3 ) , ( ( sq_row * 3 ) + 3 ) ):
						for n in range( 3 , 6 ):
							if m != j:
							#don't want to remove entries from row of interest in square
								if i in board[ m ][ n ] and ( len( board[ m ][ n ] ) > 1 ):
									board[ m ][ n ].remove( i )
					#remove i from other entries in square


			des_entries = []
			for entry in row_unsolved[ j ][ 6 : 9 ]:
				if entry != 0:
					for number in entry:
						des_entries.append( number )
			#pulls all numbers in last 3 entries in row_unsolved[ j ] into a list

			undes_entries = []
			for entry in row_unsolved[ j ][ 0 : 6 ]:
				if entry != 0:
					for number in entry:
						undes_entries.append( number )
			#pulls numbers from all other entries in row into a list

			if ( i in des_entries ) and ( i not in undes_entries ):
			#i.e. if number i (1-9) can be in last part of row but not the rest

					sq_row = ( j // 3 )

					for m in range( ( sq_row * 3 ) , ( ( sq_row * 3 ) + 3 ) ):
						for n in range( 6 , 9 ):
							if m != j:
							#don't want to remove entries from row of interest in square
								if i in board[ m ][ n ] and ( len( board[ m ][ n ] ) > 1 ):
									board[ m ][ n ].remove( i )
					#remove i from other entries in square

	return board




def main( board , max_iter ):
#takes in sudoku board and returns answer if it can be found
#will do max_iter iterations before giving up

#TEST
#	board = [ [0,0,3,0,2,0,6,0,0], [9,0,0,3,0,5,0,0,1], [0,0,1,8,0,6,4,0,0], [0,0,8,1,0,2,9,0,0], [7,0,0,0,0,0,0,0,8], [0,0,6,7,0,8,2,0,0], [0,0,2,6,0,9,5,0,0], [8,0,0,2,0,3,0,0,9], [0,0,5,0,1,0,3,0,0] ]
#TEST

	for row in board:
		for i in range( 0 , 9 ):
			if row[ i ] == 0:
				row[ i ] = [ 0, { 1, 2, 3, 4, 5, 6, 7, 8, 9 } ]
	#changes all zeroes into a list - first entry zero to indicate unsolved, 2nd entries is all possible numbers
			else:
				row[ i ] = [ 1, set( [ row[ i ] ] ) ]
	#changes all other entries into a list with a 1 (for solved) and a length-one set

	last_solved = 0

	iter = 0
	while iter < max_iter:
		iter += 1

		old_board = board
		board = solver_iteration( old_board )

		old_board = board
		board = solver_iteration_2( old_board )

#		old_board = board
#		board = solver_iteration_3( old_board )

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

		last_solved = solved_count

	print('Error: not enough iterations to solve, or solver will never converge on answer')
	return board






