#Spiral primes
#Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49

#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?






import check_prime
#check_prime.main(x) returns 0 if x not prime, 1 if x is prime




def main(frac):
#solves defined problem for length of spiral when ratio of primes on diagonal falls below frac (frac = 0.10 as defined in problem)

	size = 3
	#"length" of square
	primes = 3
	#number of primes in square
	frac_prime = primes / (size * 2 - 1)
	#fraction of primes on diagonal

	while frac_prime >= frac:
	#continues until fraction of primes on diagonal falls below frac

		size += 2
		#increases size of square

		print('size=',size)
		#TEST

		for x in range(1,4):
		#since square numbers are not prime, only needs to check the numbers added to the non-bottom right corner

			y = (size ** 2) - ( (size - 1) * x )
			#formula for the numbers of interest (new non-square corner numbers)

			primes += check_prime.main(y)
			#adds check_prime.main(y) for each number of interest to the number of primes along the diagonal - one if the number is prime, zero if it's  not

		frac_prime = primes / (size * 2 - 1)
		#recalculates fraction of primes on diagonal

		print('frac_prime=',frac_prime)
		#TEST

	return size
