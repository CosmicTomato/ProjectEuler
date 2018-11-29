#Pandigital multiples

#Take the number 192 and multiply it by each of 1, 2, and 3:

#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?






#notes:
#must start with number that is 4 digits or less

#rough idea:
#start with number
#make sure digits are all different, otherwise move to next number
#multiply by 2, append to end of original number, make sure all digits are different still, otherwise move to next number
#check if total digits == 9:
#if more than 9, stop search
#while total digits < 9:
#multiply starting number by (3,4,5,etc.) and append to end, then check if all digits are different (if not then move to next number)
#if total digits == 9:
#save starting number and final number to list
#if total digits > 9:
#move onto next number
#at end report number with highest pandigital result from list


def test( test_num ):
#returns 0 if test_num does not have desired property
#if test_num has desired property, then returns resulting 1 to 9 pandigital number

	num_str = str( test_num )
	#creates string of the test number

	num_str += str( test_num * 2 )
	#adds test number * 2 to end of string

	if num_str.count( '0' ) > 0:
	#number will not work (doesn't have desired property) if number string contains a 0

		return 0

	for i in range( 1, 10 ):
	#checks 1-9

		if num_str.count( str( i ) ) > 1:
		#i.e. if there are any repeats of digit i

			return 0

	mult = 3
	#holder index

	while len( num_str ) < 9:

		num_str += str( test_num * mult )
		#adds original number times 'mult' index to number string

		mult += 1
		#increments 'mult' index

	if len( num_str ) > 9:
	#will only work if string has exact length of 9, otherwise test number does not have desired property

		return 0

	if len( num_str ) == 9:

		if num_str.count( '0' ) > 0:
		#number will not work (doesn't have desired property) if number string contains a 0

			return 0

		for i in range( 1, 10 ):
		#checks 1-9

			if num_str.count( str( i ) ) > 1:
			#i.e. if there are any repeats of digit i

				return 0

		return int( num_str )
		#if function has not yet returned 0, then number has desired property. returns the number string as an integer


def main():
#solves defined problem

	good_starts = []
	solutions = []

	for test_num in range( 2, 10**5 ):
	#must start with number that is at least 2, and less than 5 digits

		test_result = test( test_num )
		#uses above function "test" to see if test_num has desired property

		if test_result != 0:
		#i.e. if test_num has desired property

			good_starts.append( test_num )
			solutions.append( test_result )
			#stores the starting number and the resulting pandigital

	return [ max( solutions ), good_starts[ solutions.index ( max( solutions) ) ] ]


