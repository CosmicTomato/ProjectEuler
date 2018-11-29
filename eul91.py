#Right triangles with integer coordinates

#The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

#There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
#0 ≤ x1, y1, x2, y2 ≤ 2.

#Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?



def distance( x0 , y0 , x1 , y1 ):
#calculates distance between two x/y coordinates

	x_dist = abs( x1 - x0 )
	y_dist = abs( y1 - y0 )
	dist_sq = ( x_dist ** 2 ) + ( y_dist ** 2 )
	dist = ( dist_sq ** 0.5 )
	return dist


def check_right_tri( x0 , y0 , x1 , y1 , x2 , y2 ):
#takes in coordinates of three points and determines if they form a right triangle
#returns 1 if they do, zero otherwise

#ARBITRARY TOLERANCE
	tolerance = ( 0.000001 )
#ARBITRARY TOLERANCE

	side1 = distance( x0 , y0 , x1 , y1 )
	side2 = distance( x0 , y0 , x2 , y2 )
	side3 = distance( x1 , y1 , x2 , y2 )
	sides = [ side1 , side2 , side3 ]
	sides.sort()

	if abs( ( ( sides[ 0 ] ** 2 ) + ( sides[ 1 ] ** 2 ) ) - ( sides[ 2 ] ** 2 ) ) < tolerance:
	#i.e. if right triangle
		return 1
	else:
		return 0



def main( n ):
#solves defined problem for x,y < n (as defined n = 50 )

	x0 = 0
	y0 = 0

	right_tri = 0

	for x1 in range( 0 , ( n + 1 ) ):
		for y1 in range( 0 , ( n + 1 ) ):
			for x2 in range( 0 , ( n + 1 ) ):
				for y2 in range( 0 , ( n + 1 ) ):
	#varies coordinates of the other two points

					if ( ( x1 != x0 ) or ( y1 != y0 ) ) and ( ( x2 != x0 ) or ( y2 != y0 ) ) and ( ( x1 != x2 ) or ( y1 != y2 ) ):
					#i.e. if no duplicate coordinates

						if ( ( x1 * y2 ) - ( x2 * y1 ) ) != 0 :
						#i.e. if not a line

							right_tri += check_right_tri( x0 , y0 , x1 , y1 , x2 , y2 )
							#since check_right_tri returns 1 if right triangle, zero if not
#TEST	
#							if check_right_tri( x0 , y0 , x1 , y1 , x2 , y2 ) == 1:
#								print( 'x0 , y0 , x1 , y1 , x2 , y2=', x0 , y0 , x1 , y1 , x2 , y2 )
#TEST	
	return ( right_tri / 2 )

