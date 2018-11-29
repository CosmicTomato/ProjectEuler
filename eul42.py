#Coded triangle numbers

#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?




import letter_to_number
#letter_to_number.main(x) converts x from a letter to a number




def get_triangle_numbers(x):
#gets first x triangle numbers

	tri_num = [1]

	index = 1

	while index < x:

		index += 1

		new_num = tri_num[-1] + index

		tri_num.append( new_num )

	return tri_num


def main():

#THIS SECTION DIRECTLY ADAPTED FROM eul22.py
	words_file = open('words.txt')
	#opens words.txt

	words_list = words_file.read().replace('"','').split(',')
	#creates list (words_list) containing all the words separated by commas

	words_file.close()
	#closes words.txt

	numbers_list = []
	#will hold words converted to ordered number sets

	for i in words_list:
	#takes each word

		i_list = []

		#print(i)
		#TEST

		for j in i:
		#takes each letter in word, finds it's numerical value, then puts in a list

			i_list.append( letter_to_number.main(j) )

		numbers_list.append(i_list)
		#adds list of values for each letter of a single word to the "numbers_list"

	sums_list=[]

	for i in numbers_list:
	#takes each word (currently a list of digits) and sums it into a single number

		sums_list.append( sum( i ) )
#END ADAPTED SECTION

	tri_num = get_triangle_numbers(1000)
	#gets first 1000 triangle numbers

	tri_words = 0
	#will count number of triangle words

	for i in sums_list:
	#checks the sums of all words

		if i in tri_num:
		#checks if word is a triangle word. adds 1 to tri_words if it is

			tri_words += 1

	return tri_words





