#Square root digital expansion

#It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

#The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.


#STRATEGY: USE BUILT IN PYTHON FUNCTIONS
#based on comments at https://stackoverflow.com/questions/4733173/how-can-i-show-an-irrational-number-to-100-decimal-places-in-python

import decimal
#see documentation: https://docs.python.org/3/library/decimal.html

decimal.getcontext().prec = 102
#sets decimal precision to 101 places after decimal
#extra digit allows us to avoid rounding

def main():
	ans = 0
	square_list = [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 ]
	for base in range( 1 , 101 ):
		if ( base not in square_list ):
		#i.e. if square root is irrational
			square_root = decimal.Decimal( base ).sqrt()
			#gets square root

#TEST
			print('square_root=',square_root)
#TEST
			f = str( square_root ).replace( '.' , '' )
			g = list( f )
			dec_list = []
			for h in g:
				dec_list.append( int( h ) )
			#strips out decimal point then creates list of comma-separated numbers
#TEST
			print('len(dec_list)=',len(dec_list))
#TEST
			ans += sum( dec_list[ 0 : 100 ] )

	return ans

