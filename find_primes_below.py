#find_primes_below.py
#finds all the primes below a given number (n)

#uses a sieve method (I think!)

#imports math to use sqrt func later
import math

def main(n):

	#initializing variables
	primelist=[2]
	i=1
	n=n-2

	while i<n:	#loop continues until done looking for primes below n
		i=i+2	#sets up to check next odd number for primeness

		sqrti=math.sqrt(i) #finds square root of i (only need to see if divisible by numbers up to here!)

		#checks to see if any prime found so far (that is less than or equal to sqrt(i)) divides i; stops if any divisor is found
		j=0
		while i%primelist[j] != 0 and primelist[j] <= sqrti and j < len(primelist)-1:
			j=j+1

		#if j is prime, adds it to the list of primes
		if primelist[j] > sqrti:
			primelist.extend([i])
			

	return primelist


