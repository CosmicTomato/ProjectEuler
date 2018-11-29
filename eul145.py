#How many reversible numbers are there below one-billion?

#Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

#There are 120 reversible numbers below one-thousand.

#How many reversible numbers are there below one-billion (10^9)?



def reverse_int(n):
	return int(str(n)[::-1])
#reverses a number around


def odd_digits(n):
#checks if all digits of n are odd. if yes, then returns 1; otherwise returns 0

	check = 1

	list_n = []
	str_n = str( n )
	for digit in str_n:
		list_n.append( int( digit ) )
	#block creates list of digits of n in integer form

	for i in list_n:
		if ( i % 2 ) == 0:
			check = 0
	#flips check to 0 if any digit is even (evenly divided by 2)

	return check

def main( x ):
#finds number of reversible numbers below x

	rev_num_count = 0

	for i in range( 1 , x ):

		rev_i = reverse_int( i )

		if len( str( rev_i ) ) == len( str( i ) ):
		#i.e. if no leading zero in rev_i

			test_sum = i + rev_i

			rev_num_count += odd_digits( test_sum )

	return rev_num_count

















