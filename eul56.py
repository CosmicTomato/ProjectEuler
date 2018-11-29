#A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

#Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?





import digit_sum
#digit_sum.main(x) returns the sum of the digits of x



def main(x):
#finds desired numbers for a,b < x

	max_sum = [0,0,0,0]
	#placeholder for max digital sum

	for a in range(1,x):

		for b in range(1,x):

			atob = a ** b
			#calculates and stores exponent

			digsum = digit_sum.main(atob)
			#finds sum of digits

			if digsum > max_sum[0]:
			#stores numbers if newest biggest max digital sum

				max_sum = [digsum,a,b,atob]

	return max_sum










