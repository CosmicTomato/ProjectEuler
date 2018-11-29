#Large non-Mersenne prime

#The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 2^6972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p−1, have been found which contain more digits.

#However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

#Find the last ten digits of this prime number.



##BEGIN FIRST ATTEMPT THAT DIDN'T WORK:
#7830457 is prime
#however, 7830457-1 = 7830456 = 2 * 2 * 2 * 3 * 509 * 641

#num = 28433 * 2 * ( ( ( ( ( (2**2) ** 2 ) ** 2) ** 3) ** 509) ** 641) + 1
		  #this part is 2^7830456

#print(num)
##END OF FIRST ATTEMPT



#BEGIN ATTEMPT TWO
#according to: http://www.exploringbinary.com/patterns-in-the-last-digits-of-the-positive-powers-of-two/
#the last ten digits of 2^n repeat 7812500 (for n)
#thus

num = 28433 * ( 2 ** ( 7830457 - 7812500 ) ) + 1

print( 'num=', num )



