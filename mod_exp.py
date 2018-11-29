#implements modular math exponent

def main( x , exp , base ):
#calculates ( x ** exp ) mod base

	ans = ( x % base )
	iter = 1

	while iter < exp:
		ans = ( ( ans * x ) % base )
		iter +=1

	return ans

