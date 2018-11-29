#Disc game prize fund

#A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.

#The player pays £1 to play and wins if they have taken more blue discs than red discs at the end of the game.

#If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be £10 before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original £1 paid to play the game, so in the example given the player actually wins £9.

#Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.


#NOTES:
#numerator = 1 + sum( single terms ) + sum( products of 2 terms ) + ... sum (products of 7 terms)
#where terms are numbers 1->8, but products never contain 2 of the same number
#more generally they are numbers up to the number of blue discs pulled needed to win minus one
#this accounts for all the different ways to win. the 1 is from pulling all blue discs, the single terms are from pulling all but one disc blue, etc.
#denominator = 16!
#more generally denominator = (number of turns + 1)!
#since number of discs increases by 1 each turn


import itertools
import factorial
#for use later


def prob_win( n ):
#calculates the chance of winning a game with n terms
#returns answer as numerator and denominator of fraciton (to give exact answer)

	numerator = 1
	#to cover case where all chosen discs are blue

	to_win = ( n // 2 ) + ( n % 2 )
	#finds min number of blue discs needed to win (e.g. n=15, then to_win = 8)

	poss = []
	for i in range( 1 , ( n + 1 ) ):
		poss.append( i )
	#creates list of 1 -> n

	for i in range( 1 , to_win ):
		lists = list( itertools.combinations( poss , i ) )
		#gets all combinations of poss (numbers) of length i with no repeats

		for a_list in lists:
		#gets product of list of numbers, then adds it to total numerator
			prod = 1
			for b in a_list:
				prod = prod * b
			numerator += prod

	denominator = factorial.main( n + 1 )

	return ( numerator , denominator )

#DIVIDE denominator / numerator and round down (denom//num) to get max cost where vendor still makes money (expected value of game is below 0 )
