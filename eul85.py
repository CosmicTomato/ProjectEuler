#Counting rectangles

#By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

#Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.



def rect_num( col , row ):
#calculates number of rectangles that can fit in a rectangular grid of col x row

	total = 0

	for i in range( 0 , col ):
		for j in range( 0 , row ):
			total += ( ( i + 1 ) * ( j + 1 ) )

	return total



#eul85.rect_num( 1 , 2000 ) = 2001000 > 2million
#eul85.rect_num( 3 , 1000 ) = 3003000 > 2million
#eul85.rect_num( 55 , 55 ) = 2371600 > 2million
#55**2 = 3025

def main():

	target = 2000000
	best = 1000000

	for row in range( 1 , 2001 ):
		max_col = 3025 // row
		for col in range( 1 , ( max_col + 1 ) ):

			rect = rect_num( col , row )
			if abs( rect - target ) < best:
				best = abs( rect - target )
				print( 'new best found' , best , '( row , col )=' , ( row , col ) )

	return ( best )


