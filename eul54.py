#Poker hands

#In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

#High Card: Highest value card.
#One Pair: Two cards of the same value.
#Two Pairs: Two different pairs.
#Three of a Kind: Three cards of the same value.
#Straight: All cards are consecutive values.
#Flush: All cards of the same suit.
#Full House: Three of a kind and a pair.
#Four of a Kind: Four cards of the same value.
#Straight Flush: All cards are consecutive values of same suit.
#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#The cards are valued in the order: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

#Consider the following five hands dealt to two players:

#The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

#How many hands does Player 1 win?





def card_to_num_pair(x):
#takes in a string corresponding to a card and returns a number pair corresponding to said card
#first number corresponds to number value (2->14), second number corresponds to suit
#for suits, clubs=1, diamonds=2, hearts=3, spades=4

	num_pair = [0,0]
	#empty holder to be filled with output

	if x[0] in ['2','3','4','5','6','7','8','9']:

		num_pair[0] = int( x[0] )

	elif x[0] == 'T':

		num_pair[0] = 10

	elif x[0] == 'J':

		num_pair[0] = 11

	elif x[0] == 'Q':

		num_pair[0] = 12

	elif x[0] == 'K':

		num_pair[0] = 13

	elif x[0] == 'A':

		num_pair[0] = 14

	if x[1] == 'C':

		num_pair[1] = 1

	elif x[1] == 'D':

		num_pair[1] = 2

	elif x[1] == 'H':

		num_pair[1] = 3

	elif x[1] == 'S':

		num_pair[1] = 4

	return num_pair



def input_to_hand(input):
#takes in input of the form '5H 5C 6S 7S KD' and outputs list of 5 card number pairs (using card_to_num_pair on each one)

	input = input.split()
	#splits the input string into cards

	output = []
	#will hold output

	for card in input:

		output.append( card_to_num_pair (card) )
		#converts the card to a number pair and appends it to the output list

	return output




def hand_value( hand ):
#requires input of a list 5 card number pairs, in form of output of input_to_hand( hand ) or a list containing 5 outputs of card_to_num_pair( card )
#higher score outputs are better:
#[0,2->14,2->14,2->14,2->14,2->14] = high card (0, then high card, then high card, then high card, then high card, then high card)
#[1,2->14,2->14,2->14,2->14,0]	   = one pair (1, pair card, then high card, then high card, then high card)
#[2,2->14,2->14,2->14,0,0]	   = two pair (2, higher pair card, pair card, high card, 0, 0)
#[3,2->14,2->14,2->14,0,0]	   = three of a kind (3, trio card, high card, high card, 0, 0)
#[4,2->14,0,0,0,0]		   = straight (4, high card, 0, 0, 0, 0)
#[5,2->14,2->14,2->14,2->14,2->14] = flush (5, ordered high cards)
#[6,2->14,2->14,0,0,0]		   = full house (6, trio card, duo card, 0, 0, 0)
#[7,2->14,2->14,0,0,0]		   = four of a kind (7, quartet card, high card, 0, 0, 0)
#[8,2->14,0,0,0,0]		   = straight flush (8, high card, 0, 0, 0, 0) (royal flush is just special case of straight flush)

	hand = sorted( hand )
	hand = hand[ ::-1 ]
	#sorts the hand by lowest card to highest card, then reverses then order to get highest -> lowest


	suits = []
	for i in range(0,5):
	#creates a list with just the suits of the cards

		suits.append( hand[i][1] )

	numbers = []
	for i in range(0,5):
	#creates a list with just the numbers of the cards (no suits)

		numbers.append( hand[i][0] )

	straight = 1
	#assumes hand is straight until proven otherwise

	for i in range(0,4):
	#checks if hand is straight

		if ( hand[i][0] ) - ( hand[i+1][0] ) != 1:
		#if any 2 cards in hand are not adjacent numbers, flips straight to zero (indicating hand is not a straight)

			straight = 0

	flush = 0
	#assumes hand is not a flush until proven otherwise

	for i in range(1,5):
	#checks if hand is a flush

		if suits.count(i) == 5:
		#if there's 5 of any suit, then flush = 1 (i.e. the hand is a flush)

			flush = 1

	if straight == 1 and flush == 1:
	#first hand case to check - straight flush

		return [8, hand[0][0], 0, 0, 0, 0]
		#returns 8 to reflect straight flush, then the highest card in hand (the rest must be in order)

	else:

		quartet = []
		#assumes there is not four of a kind unless proven otherwise

		for i in range(2,15):
		#want to check if quartet of any numbers

			if numbers.count(i) == 4:
			#if there is four of a kind, stores the number that there is four of a kind of.

				quartet.append( i )

		if quartet != []:
		#i.e. if four of a kind has been found

			high_cards = []

			for i in numbers:

				if i not in quartet:
				#finds high card that is not in four of a kind

					high_cards.append(i)

			return [7, quartet[0], high_cards[0], 0, 0, 0]
			#7 represents four of a kind, then the number that there is four of a kind of, then the value of the other card in hand.

	trio = [] 
	#assumes there is no three of a kind unless proven otherwise

	pairs = []
	#assumes there is no pairs of a kind unless proven otherwise

	for i in range(2,15):
	#want to check if three of a kind or pair of any numbers


		if numbers.count(i) == 3:
		#if there is three of a kind, stores the number that there is three of a kind of.

				trio.append( i )

		if numbers.count(i) == 2:
		#if there is pair(s), stores the number(s) that there is a pair of

				pairs.append( i )

	if trio != [] and pairs != []:
	#defines condition for full house

		return [6, trio[0], pairs[0], 0, 0, 0]
		#6 represents full house, then the number that there is three of a kind of, then the number that there is a pair of

	elif flush == 1:
	#if it's a flush (not a straight flush)

		return [5, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]]
		#5 represents flush, then the numbers from high to low

	elif straight ==1:
	#if it's a straight (& not a straight flush)

		return [4, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]]
		#4 represents straight, then the numbers from high to low

	elif trio != []:
	#if there is three of a kind (but not a full house)

		high_cards = []

		for i in numbers:

			if i not in trio:
			#finds high cards that are not in the three of a kind

				high_cards.append(i)

		return [3, trio[0], high_cards[0], high_cards[1], 0, 0]
		#3 represents three of a kind, then the number that there is three of a kind of, then the value of the other cards in hand

	elif len( pairs ) == 2:
	#i.e. if there are two pairs

		high_cards = []

		for i in numbers:

			if i not in pairs:
			#finds high card that is not in the pairs

				high_cards.append(i)

		return [2, max( pairs ), min( pairs ), high_cards[0], 0, 0]
		#2 represents two pair, then the number of the higher pair, then the number of the lower pair, then the value of the other card in hand
		
	elif len( pairs ) == 1:
	#i.e. if there is one pair

		high_cards = []

		for i in numbers:

			if i not in pairs:
			#finds high cards that are not in the pair

				high_cards.append(i)

		return [1, pairs[0], high_cards[0], high_cards[1], high_cards[2], 0]
		#1 represents are pair, then the number of the pair, then the remaining cards in hand from high to low

	else:
	#i.e. if there is no better hand (only high cards)

		return [0, numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]]
		#0 represents high card only, followed by card values from high to low

def compare_hand_values( hand1, hand2 ):
#compares two hands' values, outputs 1 if first hand is better, 2 if second hand is better, 0 if tie

	for i in range(0,6):
	#each hand value is a string of 2 ordered numbers. if the first is greater for either hand, it's the better hand, then the same for the second and so forth

		if hand1[i] > hand2[i]:

			return 1

		if hand1[i] < hand2[i]:

			return 2

	if hand1 == hand2:
	#last option, the hands are totally equal and its a tie

		return 0


def main():
#solves the stated problem

	player1hands = 0
	#will count number of hands player one wins

	ties = 0
	#will count number of ties. not strictly necessary for problem but interesting

	hands_file = open('poker.txt')
	#opens the file of poker hands

	hands_list = hands_file.read().split('\n')
	#creates list (hands_list) containing all the pairs of hands separated by commas
	#NOTE: hands_list[x][0:14] and hands_list[x][15:29] represent player1 and player2's hands, respectively, for the (x-1)th hand

	hands_file.close()
	#closes the file ('poker.txt')

	for i in range( 0, ( len( hands_list ) - 1 ) ):
	#loop runs for number of hands

		hand1input = input_to_hand( hands_list[i][0:14] )
		hand2input = input_to_hand( hands_list[i][15:29] )
		#gets the inputs (numerical sets of 5 numbered pairs representing cards) for each players' hand

		hand1 = hand_value( hand1input )
		hand2 = hand_value( hand2input )
		#gets the values of the hands (lists of 6 numbers valuing hand)

		outcome = compare_hand_values( hand1, hand2 )
		#compares the values of the hands. returns 1 if player 1's is better, 2 if player 2's is better, 0 if tie

		if outcome == 1:
		#counts times player 1 wins (has better hand)

			player1hands += 1

		elif outcome == 0:
		#counts times the 2 players tie

			ties += 1

	return [player1hands,ties]

