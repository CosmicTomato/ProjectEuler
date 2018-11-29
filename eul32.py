#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.




	#example splitting, returns c=['12','345']
	#a='12345'
	#b=a.partition('3')
	#c=[b[0],b[1]+b[2])





def main():

	import number_permutations
	permutations = number_permutations.main(123456789)
	#imports function and then uses it to find a list of all 1-9 pandigital sequences

	digits_list = ['1','2','3','4','5','6','7','8','9']
	#stores the digits one through nine, each as a string, for use in splitting the pandigital strings later

	good_trios = []

	for perm in permutations:
	#performs loop for each permuation

		for i in digits_list:

			parts_list = str( perm ).partition( str( i ) )
			#splits permutation at digit i

			parts_list = [ parts_list[0], (parts_list[1] + parts_list[2]) ]
			#combines the last two entries (i and whatever was after it) into a single entry

			if parts_list[0] != '' and parts_list[1] != '':
			#ignores the split if either part ends up empty

				for j in digits_list:
				#must split at a different digit than before

					if j != i:

						splits = parts_list[1].partition( str( j ) )
						#splits the second part at digit j

						trio = [parts_list[0], splits[0], (splits[1] + splits[2]) ]
						#combines the last two entries (j and whatever was after it) into a single entry

						if trio[0] != '' and trio[1] != '' and trio[2] != '':
                        			#ignores further actions if any part ends up empty

							if int(trio[0]) * int(trio[1]) == int(trio[2]):
								#stores trio if it meets the criteria

								good_trios.append(trio)

							#print(trio)
							#TEST

	return good_trios














