#LARGELY ADAPTED FROM ANSWER TO PROJECT EULER PROBLEM 74 (eul74.py)


#Square digit chains
#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

#For example,

#44 → 32 → 13 → 10 → 1 → 1
#85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

#How many starting numbers below ten million will arrive at 89?







def sq_digit_sum(x):
#splits x into its digits and sums their squares

	sum = 0

	for i in str(x):

		sum += ( int(i) ** 2 )

	return sum





def sq_cycle_end(q):
#finds end of square cycle starting with q

	sq_list = [q]

	x = sq_digit_sum( sq_list[-1] )
	#calculates square digit sum of last entry in list

	while (sq_list[-1] != 1) and (sq_list[-1] != 89):
	#continues until 1 or 89 is added to list

		sq_list.append(x)
		#adds x to end of list

		x = sq_digit_sum( sq_list[-1] )
		#calculates new x (square digit sum of last entry in list)

	return sq_list[-1]


def main(below):
#returns number of chains that end in 89 for starting numbers below (below) - as defined, below = 10**7

	num = 0
	#counts number of desired chains

	for i in range(1,below):

		print(i)
		#TEST

		if sq_cycle_end(i) == 89:
		#adds one to num if the chain ends in 89

			num += 1

	return num


