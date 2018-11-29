#Su Doku

#Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

#A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

#The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

#By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.





import new_sudoku
#new_sudoku.main( board, max_iter ) tries to solve the board in less than max_iter iterations

max_iter = 100
#NOTE: here max_iter is fixed, may need to be adjusted

import copy


def main():

	ans = 0

	f = open( 'sudoku.txt' )
	a = f.read().split('Grid')
	a.remove( '' )
	f.close()
	#pulls and formats text

	for b in range( 0 , 50 ):
	#because there are fifty boards

		chars = a[ b ][ 4 : ]
		#clips off start to get rid of unnecessary characters

		chars = chars.split( '\n' )
		#splits board characters into rows
		if ('') in chars:
			chars.remove('')

		board = [ [], [], [], [], [], [], [], [], [] ]

		for i in range( 0 , 9 ):
			for j in chars[ i ]:
				board[ i ].append( int( j ) )
		#transfers numbers into rows of board

		orig_board = copy.deepcopy( board )
#TEST
		print('orig_board=',orig_board)
#TEST

		board = new_sudoku.format_board( board )
		board = new_sudoku.main_plus_guessing( board , max_iter )
		#attempts to solve board

		int_ans = int( str(list(board[0][0])[0]) + str(list(board[0][1])[0]) + str(list(board[0][2])[0]) )
		#pulls first three numbers from board, appends them together, then turns that into an integer

		ans += int_ans

	return ans


#TECHNICALLY WORKS!!!
