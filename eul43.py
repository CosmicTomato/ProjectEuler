#Sub-string divisibility

#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.





import number_permutations
#number_permutations.main(x) returns a list of all the permutations of x


def check_property(x):
#checks the defined property of x. returns 1 if it has the property, 0 otherwise

	int_str = str(x)

	if ( int( int_str[1:4] ) ) % 2 == 0:

		if ( int( int_str[2:5] ) ) % 3 == 0:

			if ( int( int_str[3:6] ) ) % 5 == 0:

				if ( int( int_str[4:7] ) ) % 7 == 0:

					if ( int( int_str[5:8] ) ) % 11 == 0:

						if ( int( int_str[6:9] ) ) % 13 == 0:

							if ( int( int_str[7:10] ) ) % 17 == 0:

								return 1

							else:
								return 0

						else:
							return 0

					else:
						return 0

				else:
					return 0

			else:
				return 0

		else:
			return 0

	else:
		return 0



def main():
#solves given problem

	permutations = number_permutations.main(1234567890)
	#finds all 0-9 pandigital numbers

	num_with_prop = []
	#will store all numbers with desired property

	for i in permutations:

		if check_property( i ) == 1:

			num_with_prop.append( i )

	return sum( num_with_prop )








