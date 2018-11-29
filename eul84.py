#Monopoly odds

#see https://projecteuler.net/problem=84 for problem definition




import random
import copy
#built-in functions needed later


def dice_sum( max_num , dice ):
#returns sum of dice number of dice with faces 1-max_num
#e.g. dice_sum( 5 , 3 ) returns sum of 3 dice with 5-sides each

	ans = random.randint( 1 , max_num )
	i = 1
	while ( i < dice ):
		i += 1
		ans += random.randint( 1 , max_num )

	return ans


def CC( location ):
#for community chest spots
	rand = random.randint( 1 , 16 )
	if rand == 1:
		location = 0
		#GO
	elif rand == 2:
		location = 10
		#jail
	return location


def CH( location ):
#for chance spots
	rand = random.randint( 1 , 16 )
	if rand == 1:
		location = 0
		#GO
	elif rand == 2:
		location = 10
		#jail
	elif rand == 3:
		location = 11
		#C1
	elif rand == 4:
		location = 24
		#E3
	elif rand == 5:
		location = 39
		#H2
	elif rand == 6:
		location = 5
		#R1
	elif ( rand == 7 ) or ( rand == 8 ):
		if location == 7:
			location = 15
		elif location == 22:
			location = 25
		else:
			location = 5
		#move to next R (railroad)
	elif rand == 9:
		if location == 22:
			location = 28
		else:
			location = 12
		#move to next U (utility)
	elif rand == 10:
		location = location - 3
		#move back 3 spaces
	return location


def main( max_num , turns ):
#calculates the "popularity" of each square on monopoly board (ordered 0-39)
#uses probabalistic method where lots of rolls are performed and the number of times that squares are landed on is counted
#max_num equals number of faces on dice, and turns equals number of rolls simulated (higher -> more accurate)

	board = []
	for i in range( 0 , 40 ):
		board.append( 0 )
	times_visited = copy.deepcopy( board )
	approx_probs = copy.deepcopy( board )
	#creates 40-entry lists of zeroes

	board[ 2 ] = 'CC'
	board[ 17 ] = 'CC'
	board[ 33 ] = 'CC'
	#defines community chest squares

	board[ 7 ] = 'CH'
	board[ 22 ] = 'CH'
	board[ 36 ] = 'CH'
	#defines chance squares

	board[ 30 ] = 'G2J'
	#go to jail square

	location = 0
	rolls = 0
	dub_count = 0
	#start at square 0 (GO)

	while ( rolls < turns ):
		dice_1 = random.randint( 1 , max_num )
		dice_2 = random.randint( 1 , max_num )
		if dice_1 == dice_2:
		#i.e. if double is rolled
			dub_count += 0
		else:
		#reset doubles count if no double rolled
			dub_count = 0

		if dub_count == 3:
		#i.e. three doubles in a row -> go to jail
			location = 10
		else:
			location = ( ( location + dice_1 + dice_2 ) % 40 )
			#gets new location on board by moving based on dice outcome

			if ( board[ location ] == 0 ):
			#i.e. if on a square that doesn't have special rules
			#don't have to do anything else
				location = location

			elif ( board[ location ] == 'CC' ):
				location = CC( location )

			elif ( board[ location ] == 'CH' ):
				location = CH( location )

			elif ( board[ location ] == 'G2J' ):
				location = 10

		times_visited[ location ] += 1
		rolls += 1
		#records ending position of turn and increments turn number

	for i in range( 0 , 40 ):
		approx_probs[ i ] = times_visited[ i ] / turns * 100
	#calculates approximate probabilities to be on each square
	#multiplies by 100 to list percentages

#TEST
#	check = sum( approx_probs )
#	print( 'total probability=' , check )
#TEST

	return approx_probs
