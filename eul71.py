#Ordered fractions

#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

#If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

#It can be seen that 2/5 is the fraction immediately to the left of 3/7.

#By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.




#IDEA:
#want a/b < 3/7
#i.e. 7a < 3b
#7a <= 3b - 1
#a <= (3b - 1)/7 for given b


import gcd
#gcd.main( a, b ) finds the greatest common divisor of a and b. if gcd(a,b) = 1, then they are coprime (i.e. the fraction a/b is irreducible)


def main( x, y, cap ):
#solves the defined problem for fraction to the left of x/y for d<= cap
#as defined, x = 3, y = 7, cap = 10**6

	best = [ 1, 0 ]
	#will store answer

	desired = x / y
	#the number that we want to get close to

	for b in range( 2, cap+1 ):
	#checks all divisors 2 -> d

		a = ( x * b - 1) // y
		#finds the highest integer a for which a/b is less than x/y

		if a != 0:
		#necessary since gcd function will break if a = 0

			if gcd.main( a, b ) == 1:
			#need a,b to be coprime for fraction to be irreducible

#TEST
#				print('a=',a,'b=',b)
#TEST

				diff = desired - ( a / b )
				#calculates the difference between x/y and a/b. will always be positive since it is assured that a/b < x/y

				if diff < best[ 0 ]:
				#i.e. if best a/b found so far

					best [ 0 ] = diff
					best [ 1 ] = [ a, b ]
					#stores the best values found so far

	return best





