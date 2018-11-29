#created to solve project euler problem 96
#takes in unfinished sudoku board, outputs answer

#takes in unfinished sudoku board, outputs answer
#NOTE: ASSUMES BLANKS ARE MARKED/LISTED AS ZEROES


#NOTE: YOU NEED YO USE THE format_board function as well before using a solver
#see eul96.py for example implementation


import copy



def format_board( board ):
#formats initial board

#       easy board = [ [0,0,3,0,2,0,6,0,0], [9,0,0,3,0,5,0,0,1], [0,0,1,8,0,6,4,0,0], [0,0,8,1,0,2,9,0,0], [7,0,0,0,0,0,0,0,8], [0,0,6,7,0,8,2,0,0], [0,0,2,6,0,9,5,0,0], [8,0,0,2,0,3,0,0,9], [0,0,5,0,1,0,3,0,0] ]
#very hard board: [[0, 0, 0, 0, 0, 3, 0, 1, 7], [0, 1, 5, 0, 0, 9, 0, 0, 8], [0, 6, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 7, 0, 0, 0], [0, 0, 9, 0, 0, 0, 2, 0, 0], [0, 0, 0, 5, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0, 0, 2, 0], [5, 0, 0, 6, 0, 0, 3, 4, 0], [3, 4, 0, 2, 0, 0, 0, 0, 0]]
#super hard board: [[3, 0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 7, 0, 0, 0], [7, 0, 6, 0, 3, 0, 5, 0, 0], [0, 7, 0, 0, 0, 9, 0, 8, 0], [9, 0, 0, 0, 2, 0, 0, 0, 4], [0, 1, 0, 8, 0, 0, 0, 5, 0], [0, 0, 9, 0, 4, 0, 3, 0, 1], [0, 0, 0, 7, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 8, 0, 0, 6]]

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if board[ i ][ j ] == 0:
				board[ i ][ j ] = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
	#changes all zeroes into a list of all possible numbers
			else:
				board[ i ][ j ] = [ board[ i ][ j ] ]
	#changes all other (i.e. all solved) entries into length-one lists

	return board


def print_board( board ):
#prints state of board
	for i in range( 0 , 9 ):
		print( board[ i ] )


def pull_solved( board ):
#given a board, creates lists of solved numbers in rows, columns, and squares

	row_solved = [ [] , [] , [] , [] , [] , [] , [] , [] , [] ]
	col_solved = [ [] , [] , [] , [] , [] , [] , [] , [] , [] ]
	sq_solved = [ [] , [] , [] , [] , [] , [] , [] , [] , [] ]
	#initializing lists of lists of solved entries

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) == 1:
			#i.e. if square already solved

				row_solved[ i ].append( board[ i ][ j ][ 0 ] )
				( row_solved[ i ] ).sort()

				col_solved[ j ].append( board[ i ][ j ][ 0 ] )
				( col_solved[ j ] ).sort()

				sq_num = ( ( i // 3 ) * 3 ) + ( j // 3 )
				sq_solved[ sq_num ].append( board[ i ][ j ][ 0 ] )
				( sq_solved[ sq_num ] ).sort()

	return ( row_solved , col_solved , sq_solved )


def pull_unsolved( row_solved , col_solved , sq_solved ):
#gets lists of unsolved numbers from lists of solved numbers

	row_unsolved = [ [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] , [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ]
	col_unsolved = [ [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] , [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ]
	sq_unsolved = [ [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] , [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ,  [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ]

	for n in range( 0 , 9 ):
		for i in row_solved[ n ]:
			row_unsolved[ n ].remove( i )
		for j in col_solved[ n ]:
			col_unsolved[ n ].remove( j )
		for k in sq_solved[ n ]:
			sq_unsolved[ n ].remove( k )

	return ( row_unsolved , col_unsolved , sq_unsolved )


def solver_iteration( board , row_solved , col_solved , sq_solved ):
#takes in board and lists of all solved entries, then tries to reduce list of possibilities in all unsolved squares

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) != 1:
			#i.e. if number is so-far unsolved

				sq_num = ( ( i // 3 ) * 3 ) + ( j // 3 )
				conj = ( set( row_solved[ i ] ) | set( col_solved[ j ] ) | set( sq_solved[ sq_num ] ) )
				row_col_sq_list = list( conj )

				for k in row_col_sq_list:
					if ( k in ( board[ i ][ j ] ) ) and ( len( board[ i ][ j ] ) > 1 ):
					#added conditional to prevent errors
						 ( board[ i ][ j ] ).remove( k )
				#removes all solved numbers in row, column, and square from list of possibilities for space (square i,j)

				if len( board[ i ][ j ] ) == 1:
				#i.e. if square now solved

					row_solved[ i ].append( board[ i ][ j ][ 0 ] )
					row_solved[ i ].sort()
					col_solved[ j ].append( board[ i ][ j ][ 0 ] )
					col_solved[ j ].sort()
					sq_solved[ sq_num ].append( board[ i ][ j ][ 0 ] )
					sq_solved[ sq_num ].sort()
					#adds changes to lists of solved numbers

	return ( board , row_solved , col_solved , sq_solved )


def solver_iteration_2( board , row_solved , col_solved , sq_solved ):
#takes in board and looks at each unsolved entry. sees if it is the only one in it's row/column/square that can be one of the unsolved numbers (in the row/column/square)
#executes 'only square' rule as defined on http://www.sudokudragon.com/sudokustrategy.htm

	row_unsol_lists = [ [], [], [], [], [], [], [], [], [] ]
	col_unsol_lists = [ [], [], [], [], [], [], [], [], [] ]
	sq_unsol_lists = [ [], [], [], [], [], [], [], [], [] ]

#NOT NEEDED	( row_unsolved , col_unsolved , sq_unsolved ) = pull_unsolved( row_solved , col_solved , sq_solved )

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) != 1:
			#i.e. if square NOT already solved
				sq_num = ( ( i // 3 ) * 3 ) + ( j // 3 )
				for k in ( board[ i ][ j ] ):
					row_unsol_lists[ i ].append( k )
					col_unsol_lists[ j ].append( k )
					sq_unsol_lists[ sq_num ].append( k )
	#pulls all unsolved numbers from rows/cols/squares into lists. allows counting of unsolved entries

	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) != 1:
				sq_num = ( ( i // 3 ) * 3 ) + ( j // 3 )

				changed = 0
				for k in board[ i ][ j ]:
					if ( k not in row_solved[ i ] ) and ( k not in col_solved[ j ] ) and ( k not in sq_solved[ sq_num ] ):
						if ( row_unsol_lists[ i ].count( k ) == 1 ) or ( col_unsol_lists[ j ].count( k ) == 1 ) or ( sq_unsol_lists[ sq_num ].count( k ) == 1 ):
					#i.e. if the number is the only unsolved number in its row/column/square that can be that number then it must be that number. and change it to it

							if changed == 0:
							#prevents changing the same entry multiple times (shouldn't happen but whatever)
								changed = 1
								board[ i ][ j ] = [ k ]
								row_solved[ i ].append( k )
								row_solved[ i ].sort()
								col_solved[ j ].append( k )
								col_solved[ j ].sort()
								sq_solved[ sq_num ].append( k )
								sq_solved[ sq_num ].sort()
								#adds changes to lists of solved numbers

	return ( board , row_solved , col_solved , sq_solved )


def solver_iteration_3( board , row_solved , col_solved , sq_solved ):
#takes in board, looks for sub-group exclusions to eliminate possiblities in unsolved entries
#see http://www.sudokudragon.com/sudokustrategy.htm

	sub_groups_row = [ [], [], [], [], [], [], [], [], [] ]
	sub_groups_col = [ [], [], [], [], [], [], [], [], [] ]
	#each entry will store 3 pairs, with each pair containing the solved and unsolved entries of its row/col subsection
	#e.g. sub_groups_row[ 3 ][ 2 ][ 1 ] = the unsolved entries in the "2nd" (0-2) subsection of the "3rd" (0->8) row

	for i in range( 0 , 9 ):
	#done for each row
		for sect_num in range( 0 , 3 ):
		#done for the 3 sub-sections (each of 3 row entries) in the row

			section_solved = []
			section_unsolved = []

			for j in range( (sect_num * 3) , (sect_num * 3 + 3) ):
				if len( board[ i ][ j ] ) == 1:
					for poss in ( board[ i ][ j ] ):
						section_solved.append( poss )
				else:
					for poss in ( board[ i ][ j ] ):
						section_unsolved.append( poss )

			( sub_groups_row[ i ] ).append( [ section_solved , section_unsolved ] )

	for j in range( 0 , 9 ):
		for sect_num in range( 0 , 3 ):

			section_solved = []
			section_unsolved = []

			for i in range( (sect_num * 3) , (sect_num * 3 + 3) ):
				if len( board[ i ][ j ] ) == 1:
					for poss in ( board[ i ][ j ] ):
						section_solved.append( poss )
				else:
					for poss in ( board[ i ][ j ] ):
						section_unsolved.append( poss )

			( sub_groups_col[ j ] ).append( [ section_solved , section_unsolved ] )

#have finished pulling subgroups

	for i in range( 0 , 9 ):
		for sect_num in range( 0 , 3 ):
			section_unsolved = sub_groups_row[ i ][ sect_num ][ 1 ]

			rest_unsolved = []
			for k in range( 0 , 3 ):
				if k != sect_num:
					for entry in sub_groups_row[ i ][ k ][ 1 ]:
						rest_unsolved.append( entry )
			#gets all the unsolved numbers from the rest of the row (other than the sub-section of interest)

			for poss in range( 1 , 10 ):
				if poss in section_unsolved:
					if ( poss not in rest_unsolved ) and ( poss not in ( row_solved[ i ] ) ):
					#i.e. if unsolved number 'poss' can only be in a specific sub-section of the row, then we want to delete it from the other rows in the square that contains the row sub-section

						sq_row = ( i // 3 )
						for m in range( sq_row * 3 , sq_row * 3 + 3):
							for n in range( sect_num * 3 , sect_num * 3 + 3 ):
						#m,n label rows and columns of square of interest

								if m != i:
								#don't want to remove entries from row of interest in square

									if ( poss in board[ m ][ n ] ) and ( len( board[ m ][ n ] ) !=  1 ):
#TEST
#										print('row part modifying')
#										print('row=', board[ i ] )
#										print('section_num=',sect_num)
#										print('(m,n)=',(m,n))
#										print('poss=',poss,'board[ m ][ n ]=',board[ m ][ n ])
#TEST
										board[ m ][ n ].remove( poss )
									#remove poss from other entries in square (those not in the row being examined)
										if len( board[ m ][ n ] ) == 1:
										#i.e. if square now solved
											sq_num = ( ( m // 3 ) * 3 ) + ( n // 3 )
											row_solved[ m ].append( board[ m ][ n ][ 0 ] )
											row_solved[ m ].sort()
											col_solved[ n ].append( board[ m ][ n ][ 0 ] )
											col_solved[ n ].sort()
											sq_solved[ sq_num ].append( board[ m ][ n ][ 0 ] )
											sq_solved[ sq_num ].sort()
											#adds changes to lists of solved numbers


	for j in range( 0 , 9 ):
		for sect_num in range( 0 , 3 ):
			section_unsolved = sub_groups_col[ j ][ sect_num ][ 1 ]
			rest_unsolved = []
			for k in range( 0 , 3 ):
				if k != sect_num:
					for entry in sub_groups_col[ j ][ k ][ 1 ]:
						rest_unsolved.append( entry )
			for poss in range( 1 , 10 ):
				if poss in section_unsolved:
					if ( poss not in rest_unsolved ) and ( poss not in ( col_solved[ j ] ) ):
						sq_col = ( j // 3 )
						for n in range( sq_col * 3 , sq_col * 3 + 3):
							for m in range( sect_num * 3 , sect_num * 3 + 3 ):
								if n != j:
									if ( poss in board[ m ][ n ] ) and ( len( board[ m ][ n ] ) !=  1 ):
#TEST
#										print('col part modifying')
#										print('section_num=',sect_num)
#										print('(m,n)=',(m,n))
#										print('poss=',poss,'board[ m ][ n ]=',board[ m ][ n ])
#TEST
										board[ m ][ n ].remove( poss )
										if len( board[ m ][ n ] ) == 1:
											sq_num = ( ( m // 3 ) * 3 ) + ( n // 3 )
											row_solved[ m ].append( board[ m ][ n ][ 0 ] )
											row_solved[ m ].sort()
											col_solved[ n ].append( board[ m ][ n ][ 0 ] )
											col_solved[ n ].sort()
											sq_solved[ sq_num ].append( board[ m ][ n ][ 0 ] )
											sq_solved[ sq_num ].sort()

	return ( board , row_solved , col_solved , sq_solved )




def solver_iteration_4( board , row_solved , col_solved , sq_solved ):
#takes in board, looks for "naked twins(/triplets/etc.)" and uses them to reduce the possibilities contained in other squares
#see http://www.sudokudragon.com/sudokustrategy.htm

	#process for rows
	for i in range( 0 , 9 ):
		for j in range( 0 , 9 ):
			if len( board[ i ][ j ] ) > 1:
				if board[ i ].count( board[ i ][ j ] ) == len( board[ i ][ j ] ):
					repeat_set = copy.deepcopy( board[ i ][ j ] )

					#performs deletions
					for k in range( 0 , 9 ):
						if ( ( board[ i ][ k ] ) != ( repeat_set ) ) and ( len( board[ i ][ k ] ) > 1 ):
							for q in ( repeat_set ):
								if q in ( board[ i ][ k ] ):
									( board[ i ][ k ] ).remove( q )
									if len( board[ i ][ k ] ) == 1:
									#i.e. if sqaure now solved
										sq_num = ( ( i // 3 ) * 3 ) + ( k // 3 )
										row_solved[ i ].append( board[ i ][ k ][ 0 ] )
										row_solved[ i ].sort()
										col_solved[ k ].append( board[ i ][ k ][ 0 ] )
										col_solved[ k ].sort()
										sq_solved[ sq_num ].append( board[ i ][ k ][ 0 ] )
										sq_solved[ sq_num ].sort()
#TEST
#									print('board[ i ][ k ] now=',board[ i ][ k ])
#TEST

	#process for columns
	for j in range( 0 , 9 ):
		column = []
		for q in range( 0 , 9 ):
			column.append( board[ q ][ j ] )
		for i in range( 0 , 9 ):
			if len( board[ i ][ j ] ) > 1:
				if column.count( board[ i ][ j ] ) == len( board[ i ][ j ] ):
					repeat_set = copy.deepcopy( board[ i ][ j ] )

					#performs deletions
					for k in range( 0 , 9 ):
						if ( ( board[ k ][ j ] ) != ( repeat_set ) ) and ( len( board[ k ][ j ] ) > 1 ):
							for q in ( repeat_set ):
								if q in ( board[ k ][ j ] ):
									( board[ k ][ j ] ).remove( q )
									if len( board[ k ][ j ] ) == 1:
									#i.e. if sqaure now solved
										sq_num = ( ( k // 3 ) * 3 ) + ( j // 3 )
										row_solved[ i ].append( board[ k ][ j ][ 0 ] )
										row_solved[ i ].sort()
										col_solved[ j ].append( board[ k ][ j ][ 0 ] )
										col_solved[ j ].sort()
										sq_solved[ sq_num ].append( board[ k ][ j ][ 0 ] )
										sq_solved[ sq_num ].sort()
	#process for squares
	for sq in range( 0 , 9 ):
		square = []
		for i in range( 3 * ( sq // 3 ) , ( 3 * ( sq // 3 ) + 3 ) ):
			for j in range( 3 * ( sq % 3 ) , ( 3 * ( sq % 3 ) + 3 ) ):
				square.append( board[ i ][ j ] )
		for spot in square:
			if len( spot ) > 1:
				if square.count( spot ) == len( spot ):
					repeat_set = copy.deepcopy( spot )

					#performs deletions
					for i in range( 3 * ( sq // 3 ) , ( 3 * ( sq // 3 ) + 3 ) ):
						for j in range( 3 * ( sq % 3 ) , ( 3 * ( sq % 3 ) + 3 ) ):
							if ( ( board[ i ][ j ] ) != ( repeat_set ) ) and ( len( board[ i ][ j ] ) > 1 ):
								for q in ( repeat_set ):
									if q in ( board[ i ][ j ] ):
										( board[ i ][ j ] ).remove( q )
										if len( board[ i ][ j ] ) == 1:
										#i.e. if sqaure now solved
											sq_num = sq
											row_solved[ i ].append( board[ i ][ j ][ 0 ] )
											row_solved[ i ].sort()
											col_solved[ j ].append( board[ i ][ j ][ 0 ] )
											col_solved[ j ].sort()
											sq_solved[ sq_num ].append( board[ i ][ j ][ 0 ] )
											sq_solved[ sq_num ].sort()

	return ( board , row_solved , col_solved , sq_solved )


def check_imposs( board , row_solved , col_solved , sq_solved ):
#returns error if board cannot possibly have the solved entries that it currently does

	for k in range( 0 , 9 ):
		for poss in range( 1 , 10 ):
			if ( row_solved[ k ].count( poss ) > 1 ) or ( col_solved[ k ].count( poss ) > 1 ) or ( sq_solved[ k ].count( poss ) > 1 ):
				print('ERROR, CURRENT BOARD STATE IS IMPOSSIBLE')

def check_poss( board ):
#returns False if board cannot possibly have the solved entries that it currently does

	( row_solved , col_solved , sq_solved ) = pull_solved( board )
	for k in range( 0 , 9 ):
		for poss in range( 1 , 10 ):
			if ( row_solved[ k ].count( poss ) > 1 ) or ( col_solved[ k ].count( poss ) > 1 ) or ( sq_solved[ k ].count( poss ) > 1 ):
				return False
	return True


def main( board , max_iter ):
#takes in sudoku board and returns answer if it can be found
#will do max_iter iterations before giving up

#NEED TO DO THIS BUT NOT INSIDE FUNCTION	board = format_board( board )
#	board = format_board( board )
	( row_solved , col_solved , sq_solved ) = pull_solved( board )
	iter = 0

	while iter < max_iter:
		iter += 1

		routine_1 = 0
		while routine_1 == 0:
			old_board = copy.deepcopy( board )
			( board , row_solved , col_solved , sq_solved ) = solver_iteration( board , row_solved , col_solved , sq_solved )
			( board , row_solved , col_solved , sq_solved ) = solver_iteration_2( board , row_solved , col_solved , sq_solved )
			check_imposs( board , row_solved , col_solved , sq_solved )
			if board == old_board:
				routine_1 = 1
		#uses first and second solvers until they aren't getting anywhere anymore

#		print('before solver 3 board=')
#		print_board( board )
		( board , row_solved , col_solved , sq_solved ) = solver_iteration_3( board , row_solved , col_solved , sq_solved )
#		print('after solver 3 board=')
#		print_board( board )
#T		check_imposs( board , row_solved , col_solved , sq_solved )
		( board , row_solved , col_solved , sq_solved ) = solver_iteration_4( board , row_solved , col_solved , sq_solved )
#		print('after solver 4 board=')
#		print_board( board )
#T		check_imposs( board , row_solved , col_solved , sq_solved )

		solved_count = 0
		for i in range( 0 , 9 ):
			for j in range( 0 , 9 ):
				if len( board[ i ][ j ] ) == 1:
				#i.e. if square i,j is solved
					solved_count += 1
		if solved_count == 81:
#FOR READABILITY WHILE TESTING
			print_board( board )
#FOR READABILITY WHILE TESTING
			return ( board , True )
			#True represents that board has been solved

		if board == old_board:
#FOR READABILITY WHILE TESTING
			print_board( board )
#FOR READABILITY WHILE TESTING
			return ( board , False )
			#False since board has not been solved

	print('Error: likely not enough iterations to solve. board=')
	print_board( board )
	return board


def pull_next_guess_square( board , a , b ):
#finds first unsolved square at a,b or past

	found = False

	j = b
	for i in range( a , 9 ):
		if len( board[ i ][ j ] ) > 1:
		#i.e. if square i,j is unsolved
			found = True
			return ( i , j )

	for i in range( 0 , 9 ):
		for j in range( ( b + 1 ) , 9 ):
			if len( board[ i ][ j ] ) > 1:
			#i.e. if square i,j is unsolved
				found = True
				return ( i , j )

	if not found:
		return ( 100 , 100 )
	#NOTE: RETURNS RIDICULOUS RESULT IF WHOLE BOARD IS SOLVED


def main_plus_guessing( board , max_iter ):
#adds in guessing as method to solve very difficult boards

	( board , success ) = main( board , max_iter )
	if ( success ):
	#i.e. if board already solved
		return board

	else:
	#i.e. board not solved yet

		orig_board = copy.deepcopy( board )
		#makes copy of progress on board so far

		( a , b ) = pull_next_guess_square( board , 0 , 0 )
		#pulls first unsolved square in board

		ab_poss = copy.deepcopy( board[ a ][ b ] )
		#pulls the possibilities for square a,b
		#want to guess each one until either board is solved or possibilities are exhausted

		for poss in ab_poss:
			board = copy.deepcopy( orig_board )
			board[ a ][ b ] = [ poss ]
#LINE NOT WORKING
			( board , success ) = main( board , max_iter )
#LINE NOT WORKING --- NOT  DESIGNED FOR FEEDING BACK INTO
			if ( success ) and check_poss( board ):
	#FOR READABILITY WHILE TESTING
				print_board( board )
	#FOR READABILITY WHILE TESTING
				return ( board )

	#IF WE REACH HERE THEN GUESSING THE FIRST SQUARE HAS FAILED
	print('PROCESS HAS FAILED! WORK HARDER!')
	return board



#REMOVED BELOW
#added for below function
#import itertools
#possibles = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
#a = list( itertools.combinations( possibles , 2 ) )
#two_lens = []
#for b in a:
#	two_lens.append( list( b ) )
#creates a list that creates 2-length lists of all combinations of entries


