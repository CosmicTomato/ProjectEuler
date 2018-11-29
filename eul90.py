#Cube digit pairs


#Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

#For example, the square number 64 could be formed:

#In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

#For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

#However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

#In determining a distinct arrangement we are interested in the digits on each cube, not the order.

#{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
#{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

#But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

#How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?




#squares_list = [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 ]
#note: 6 is equivalent to 9, 19 is equivalent to 16, 39 is equivalent to 36, 46 is equivalent to 49, 94 is equivalent to 64
#NOTE: IF CUBE HAS 6 OR 9 ON IT, IT ACTS AS IF IT HAS BOTH ON IT


import copy
import itertools


def main():

	ans = 0

	poss_faces = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
	#list of numbers that can be on face of cube
	poss_cubes = list( itertools.combinations( poss_faces , 6 ) )
	#creates list of tuples of all combinations of numbers that can appear on a cube

	for i in range( 0 , len( poss_cubes ) ):
		poss_cubes[ i ] = list( poss_cubes[ i ] )
		#converts all entries to lists

		if ( 6 in poss_cubes[ i ] ) and ( 9 not in poss_cubes[ i ] ):
			poss_cubes[ i ].append( 9 )
		elif ( 9 in poss_cubes[ i ] ) and ( 6 not in poss_cubes[ i ] ):
			poss_cubes[ i ].append( 6 )
		#adds 6 or 9 to cube if it has one and not the other
#TEST
	print('poss_cubes=',poss_cubes)		
#TEST

	for i in range( 0 , len( poss_cubes ) ):
		for j in range( 0 , len( poss_cubes ) ):
			if ( j >= i ):
			#gets rid of duplicates
				squares_list = [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 ]
				for face_1 in poss_cubes[ i ]:
					for face_2 in poss_cubes[ j ]:
						num = int( str( face_1 ) + str( face_2 ) )
						if num in squares_list:
							squares_list.remove( num )
						num = int( str( face_2 ) + str( face_1 ) )
						if num in squares_list:
							squares_list.remove( num )
		#start with list of all squares below 100. use combo of two cubes, check all combos of faces. remove all squares from list as they are found
				if squares_list == []:
				#i.e. if all squares found with this cube combination
					ans += 1
#TEST
					print('cube_1=',poss_cubes[ i ])
					print('cube_2=',poss_cubes[ j ])
#TEST

	return ans

