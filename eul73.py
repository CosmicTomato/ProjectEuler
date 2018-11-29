#Counting fractions in a range

#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

#If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

#It can be seen that there are 3 fractions between 1/3 and 1/2.

#How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?





import gcd
#gcd.main( a, b ) finds the greatest common divisor of a and b. if gcd(a,b) = 1, then they are coprime (i.e. the fraction a/b is irreducible)


#want to search in space:
#a/b > c/d
#i.e. ad > bc
#ad >= bc + 1
#i.e. a >= (bc // d) + 1
#and a/b < e/f
#i.e. af < be
#af <= be - 1
#i.e. a <= (be - 1) // f


#so, for a given b, want to look for fractions of form a/b where:
#a is between (bc+1)//d and (be-1)//f
#check if gcd(a,b)=1, if yes then (a/b) is an irreducible fraction


def main( frac_floor1, frac_floor2 , frac_ceil1, frac_ceil2, d ):
#solves the defined problem
#as given, frac_floor1 = 1, frac_floor2 = 3, frac_ceil1 = 1, frac_ceil2 = 2, d = 12000

	frac_num = 0
	#will count number of irreducible fractions

	for b in range( 2, ( d + 1 ) ):
	#want to check all denominators 2 to d

		for a in range( ( ( (b * frac_floor1 ) // frac_floor2 ) + 1 ), ( ( ( (b * frac_ceil1 ) - 1 ) // frac_ceil2 ) + 1 ) ):
		#see above calculations for cap and floor on a

#TEST
			print('a=',a,'b=',b)
#TEST
#BOUNDS ARE INCORRECT

			if gcd.main( a, b ) == 1:
			#i.e. if a/b is an irreducible fraction, then add one to the fraction count

				frac_num += 1

	return frac_num

