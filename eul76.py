#Counting summations


#It is possible to write five as a sum in exactly six different ways:

#4 + 1
#3 + 2
#3 + 1 + 1
#2 + 2 + 1
#2 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1

#How many different ways can one hundred be written as a sum of at least two positive integers?



#SEE WIKIPEDIA PAGE FOR PARTITION FUNCTION:
#https://en.wikipedia.org/wiki/Partition_(number_theory)


#project euler problem is written so answer is partition function minus one

def main ( x ):
#finds number of ways to write x

	if x < 2:

		return 'error'

	else:

		summation = []
		for j in range( 0 , x ):
			summation.append(0)
		#creates empty list with x entries

		for i in range ( 0 , ( x + 1 ) ):
		#can have from zero to x ones in sum

			summation [ 1 ] = i
			#i.e. number of 1's in sum

			for j in range ( 1 , x ):
			#can add numbers from 1 to (x-1) to form sums

				sum_tot = 0
				for k in range ( 0 , len ( summation ) ):
				#calculates the sum so far by multiplying each integer(k) by the number of times it appears in the sum (summation[k])

					sum_tot += summation [ k ]  * k

				remainder = x - sum_tot

