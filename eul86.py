#Cuboid route


#A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.

#However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

#It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

#Find the least value of M such that the number of solutions first exceeds one million.



#NOTE: ANOTHER PROBLEM INVOLVING PYTHAGOREAN TRIPLES
#TREAT CUBE AS FLAT SURFACE (RECTANGLE)
#X x Y x Z >>>> X x (Y x Z) or (X x Y) x Z or (X x Y) x Z
#number outside of parentheses is equal to largest individual side!
#might not even have to worry about this and be able to count solutions directly


import pythag_trips
import copy

def num( max_side ):
#finds number of solutions for cuboid of side lengths all less than or equal to max_side

	ans = 0

	pythag_base = pythag_trips.main( max_side * 10 )
	#finds all reduced pythagorean triples with total length less than 10*max_side

	general_trips = []
	for pythag_set in pythag_base:
		set_copy = copy.deepcopy( pythag_set )
		set_copy.sort()
		set_append = [ 0 , 0 , 0 ]
		mult = 1
		while ( mult * set_copy[ 0 ] ) <= max_side:
			for i in range( 0 , 3 ):
				set_append[ i ] = ( mult * set_copy[ i ] ) 
			general_trips.append( copy.deepcopy( set_append ) )
			mult += 1

#TEST
#	print('general_trips=',general_trips)
#TEST

#shortest path will be third entry in one of these triples
#longest side of cuboid will be one of the other two entries. the other two cuboid sides will add up to the third entry, BUT they both must individually be shorter (or equal to) the longest side

	for triplet in general_trips:
		triplet.sort()
		#sorts triplet small -> large

		if triplet[ 0 ] <= max_side:
			if ( triplet[ 1 ] - 1 ) < ( 2 * triplet[ 0 ] ):
			#assumes longest side is 0-th entry. there are zero possible cuboids if the defined condition is not met
			#the other two sides must add up to the first entry ( triplet[ 1 ] )
			#other sides can be up to equal to 0-th entry

				cuboids = ( ( ( triplet[ 0 ] * 2 ) - triplet[ 1 ] ) // 2 ) + 1
				ans += cuboids
				#counts number of possible cuboids
#TEST
#				print('triplet',triplet)
#				print('cuboids with longest side of 0th entry=',cuboids)
#TEST

		if triplet[ 1 ] <= max_side:
			cuboids = ( triplet[ 0 ] // 2 )
			ans += cuboids
			#counts number of possible cuboids when longest side is 1st entry
			#this is also the number of ways the other two sides can add up to the 0-th entry

#TEST
#			print('triplet',triplet)
#			print('cuboids with longest side of 1st entry=',cuboids)
#TEST
	return ans









def unused( max_side):

	tolerance = 0.00000001
	ans = 0

	for i in range( 1 , ( max_side + 1 ) ):
		for j in range( i , ( max_side + 1 ) ):
			for k in range( j , ( max_side + 1 ) ):
				# k >= j >= i

				num = ( k ** 2 ) + ( ( j + i ) ** 2 )
				sq_rt = num ** 0.5

				if abs( sq_rt - int( sq_rt ) ) < tolerance:
					ans += 1
					print( 'sides are: ' , [ i , j , k ] )
					print( 'i+j,k=',(i+j),k )


	return ans


def main( des ):
#solves defined problem for solutions >= des
#as defined des = 10**6

	result = 0
	max_side = 0

	while result < des:
		max_side += 1
		result = num( max_side )

		print( 'max_side = ',max_side)
		print('result=',result)

	return max_side


