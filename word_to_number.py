#takes a word input, splits it up into letters, finds the numerical value of each letter and sums them


import letter_to_number
#letter_to_number.main(x) returns numerical value of the letter x



def main(word):

	sum = 0

	for i in word:

		sum += letter_to_number.main( i )

	return sum






















