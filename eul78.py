#Coin partitions

#Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
#OOOOO
#OOOO   O
#OOO   OO
#OOO   O   O
#OO   OO   O
#OO   O   O   O
#O   O   O   O   O

#Find the least value of n for which p(n) is divisible by one million.



#notes:
#p(2) = 1
#O O
#p(3) = 2
#O O O and O OO
#p(4) = 5
#O O O O, O O OO, OO OO, O OOO, OOOO
#p(5) = 7
#see above
#p(6) = 11
#O O O O O O, O O O O OO, O O OO OO, OO OO OO,  O O O OOO, O OO OOO, OOO OOO, O O OOOO, OO OOOO, O OOOOO, OOOOOO

#P(N) EQUALS THE NUMBER OF POSSIBLE SUMS THAT MAKE N (INCLUDING ITSELF)


import partition_numbers
#partition_numbers.find_partition_nums( n ) finds the first n partition numbers


def main ( x, cap ):
#solves the defined problem. as written, x = one million (10**6)
#cap is cap on search

	partition_nums = partition_numbers.find_partition_nums( cap )

	check = 0

	for i in range( 1, len( partition_nums ) ):
#TEST
		print('i=',i)
		print('partition_nums[ i ]=',partition_nums[ i ])
#TEST
		if partition_nums[ i ] % x == 0:
			return partition_nums[ i ]


	return i




