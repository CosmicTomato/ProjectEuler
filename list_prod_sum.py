#takes two lists a multiplies them pairwise. returns the sum.
#e.g. [1,2,3] * [4,5,7] = 1 * 4 + 2 * 5 + 3 * 7 = 35
#for uneven length lists, just multiplies as many numbers as possible (i.e. length of shorter list)

def main( a , b ):

	fin_sum = 0

	max_len = min( len(a), len(b) )

	for i in range( 0 , max_len ):

		fin_sum += ( a[i] * b[i] )

	return fin_sum



