#Almost equilateral triangles

#It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

#We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

#Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).


#SIMILAR TO PROBLEM 75
#problem is based around Pythagorean triples. see wikipedia: https://en.wikipedia.org/wiki/Pythagorean_triple


import pythag_trips
#pythag_trips.main( x ) returns a list of all primitive pythagorean triples below x


def main( n ):
#solves problem for perimeter up to length n
#as defined n = 10**9

	primitive_trips = pythag_trips.main( 2 * n )
	#finds all primitive triplets of total length < 2n

	per_sum = 0

	for triplet in primitive_trips:
		triplet.sort()
		#puts triplet in ascending order
		perimeter = ( ( 2 * triplet[ 0 ] ) + ( 2 * triplet[ 2 ] ) )
		if perimeter <= n:

			#triplet[ 0 ] is half the length of the side that is not equal to the others. therefore triplet[0]*2(+or-)1 should equal triplet[2]
			#triplet[1] is then the length of the perpendicular bisector of the triangle

			if ( ( triplet[ 0 ] * 2 - 1 ) == triplet[ 2 ] ) or ( ( triplet[ 0 ] * 2 + 1 ) == triplet[ 2 ] ):
				per_sum += perimeter
#TEST
				print( 'sides are', ( 2 * triplet[ 0 ] ) , ( triplet[ 2 ] ) )
#TEST

	return per_sum

