#Singular integer right triangles

#It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

#12 cm: (3,4,5)
#24 cm: (6,8,10)
#30 cm: (5,12,13)
#36 cm: (9,12,15)
#40 cm: (8,15,17)
#48 cm: (12,16,20)

#In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

#120 cm: (30,40,50), (20,48,52), (24,45,51)

#Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?





#problem is based around Pythagorean triples. see wikipedia: https://en.wikipedia.org/wiki/Pythagorean_triple
#need to search through all lengths, determine which are equal to the sum of exactly one Pythagorean triple (and not more)
#or: start with primitive Pythagorean triples. find multiples below max length. then delete any duplicates, and finally count the number of entries



import pythag_trips
#pythag_trips.main( x ) returns a list of all primitive pythagorean triples below x


def main( x ):
#finds the number of values of L <= x for which exactly one integer sided right triangle can be formed

	primitive_trips = pythag_trips.main( x )
	#finds all primitive triplets of total length < x

	possible_lengths = []
	#will hold the counts of possible lengths to be made by the triplets

	for i in range( 1 , x+2 ):
	#fills possible_lengths with (x+1) zeroes.
	#possible_length[y] will equal the number of ways to make y

		possible_lengths.append( 0 )

	for i in range( 0 , len( primitive_trips ) ):
	#want to to calculation for all primitive triplets

		triplet = primitive_trips[ i ]
		#pulls the triplet out of the list

		trip_length = sum( triplet )
		#finds length of triplet

		length = trip_length

		while length <= x:
		#iterates until length > max length

			possible_lengths[ length ] += 1
			#adds one to the count of the number of ways to make (length)

			length += trip_length
			#increases length by amount of one triplet (equivalent to multiplying trip_length by the next integer)

	singles = possible_lengths.count( 1 )
	#will count number of lengths that can be made in exactly one way


#TEST
#	print (possible_lengths)
#TEST

	return singles




