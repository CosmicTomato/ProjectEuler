#finds all the permutations of a number


import itertools #imports built in itertools for use later

def main(x):

	a = itertools.permutations(str(x))
	a = [int(''.join(x)) for x in a]
	#gets permutations and formats correctly

	a = list(set(a))
	#gets rid of duplicates


	
	a=filter(lambda y: len(str(y)) == len(str(x)),a)
	#uses built-in filter function to get rid of shorter numbers (that don't have the same number of digits)

	a=list(a)
	#reformats a to correctly be a list


	return a


