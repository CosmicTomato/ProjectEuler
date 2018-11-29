#Square root convergents
#It is possible to show that the square root of two can be expressed as an infinite continued fraction.

#√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

#By expanding this for the first four iterations, we get:

#1 + 1/2 = 3/2 = 1.5
#1 + 1/(2 + 1/2) = 7/5 = 1.4
#1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

#The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

#In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?


def main(d):
#solves desired problem for first d expansions

	#first expansion
	i = 1
	#iteration/expansion number
	num = 3
	denom = 2

	more_dig = 0
	#counts desired fractions

	while i < d:
	#loop continues through all desired expansions

		i +=1
		#increases iteration/expansion number by one

		old_denom = denom
		#placeholder to store number for calculations

		denom = num + denom
		#new denominator is the old numerator + the old denominator

		num = old_denom + denom
		#new numerator is the old denominator + the new denominator (i.e. 2x the old denominator + the old numerator)

		if len( str( num ) ) > len( str( denom) ):
		#adds one to count of desired fractions if current fraction meets the criteria

			more_dig += 1


	return more_dig





