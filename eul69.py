#Totient maximum

#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

#n	Relatively Prime	φ(n)	n/φ(n)
#2	1	1	2
#3	1,2	2	1.5
#4	1,3	2	2
#5	1,2,3,4	4	1.25
#6	1,5	2	3
#7	1,2,3,4,5,6	6	1.1666...
#8	1,3,5,7	4	2
#9	1,2,4,5,7,8	6	1.5
#10	1,3,7,9	4	2.5
#It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

#Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.



import import_primes
#import_primes.main() pulls all primes less than one million

def main( x ):
#finds number less than or equal to x (in problem x = one million) that contains the most prime factors
#this number solves the desired problem -- see wikipedia page

	primes = import_primes.main()
	#pulls list of primes less than one million

	i = 0

	num = 2

	while num <= x:
	#multiples number by primes until it is greater than x

		i += 1

		num = num * primes[i]
		#multiply number by next prime

	num = num // primes[i]
	#divides out last prime number that was multiplied, to return number to below x

	return num


