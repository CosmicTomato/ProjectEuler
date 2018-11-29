#Double-base palindromes

#The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)



import number_palindrome
#number_palindrome.main(x) returns an integer that is the palindrome of x




def main(x):
#solves the problem for numbers less than x

	num_sum = 0
	#initializing

	for i in range( 1, x ):
	#want to check all numbers less than x

		if number_palindrome.main( i ) == i:
		#loop only executes if number is a palindrome (in base 10)

			bin_num = int( bin(i)[2:] )
			#creates integer with the binary digits of i

			if number_palindrome.main( bin_num ) == bin_num:
			#only execures if number is palindrome in binary

				num_sum += i
				#adds i to sum if it is a palindrome in both base 10 and binary

	return num_sum










