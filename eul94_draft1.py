#Almost equilateral triangles

#It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).



def main( n ):
#solves problem for shared side up to length n
#as defined n = 333,333,333

	per_sum = 0

#ARBITRARY TOLERANCE
	tolerance = 0.0000001
#ARBITRARY TOLERANCE

	for shared_side in range( 2 , ( n + 1 ) ):
		for other_side in [ ( shared_side - 1 ) , ( shared_side + 1 ) ]:
			if ( shared_side % 2 ) == 1:
				bisect = ( ( shared_side ** 2 ) - ( ( other_side / 2 ) ** 2 ) ) ** 0.5
				if abs( bisect - int( bisect ) ) < tolerance:
					per_sum += ( ( 2 * shared_side ) + other_side )
#TEST
					print('shared_side=', shared_side , 'other_side=' , other_side )
#TEST

	return per_sum

