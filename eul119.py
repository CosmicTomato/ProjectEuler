#Digit power sum

#The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number with this property is 614656 = 28^4.

#We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

#You are given that a2 = 512 and a10 = 614656.

#Find a30.






#SOLUTION AS WRITTEN IS NOT FAST ENOUGH
#PERHAPS START FROM EXPONENTS SOMEHOW?
#WOULD HELP TO HAVE FAST WAY TO ORDER EXPONENTS







def main( n ):
#finds first n numbers in desired list
#problem as stated just wants n=30

	a_list = []
	max_exp = 10

	i = 2
	#since 1 is not included in the list for problem statement

	while len( a_list ) < n:
	#keeps searching until n found

		exp = 2

		i_list = list( str( i ) )
		i_sum = 0
		for j in i_list:
			i_sum += int( j )
		#finds sum of digits of i

		while exp <= max_exp:

			if ( i_sum ** exp ) == i:

				a_list.append( i )
				exp = max_exp + 1
				#2nd part is to ensure while loop ends

#TEST
				print('a_list len=',len(a_list))
#TEST

			else:
				exp += 1

		i += 1
		#increments i

	return a_list










