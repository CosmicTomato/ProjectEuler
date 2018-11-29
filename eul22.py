#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?



import letter_to_number
#letter_to_number.main(x) returns numerical value of the letter x


#NOT NECESSARY
#import word_to_number
#word_to_number.main(x) returns numerical value of the sum of each letter of x
#NOT NECESSARY


def main():

	names_file = open('names.text')
	#opens names.text

	names_list = names_file.read().replace('"','').split(',')
	#creates list (names_list) containing all the names separated by commas

	names_file.close()
	#closes names.text

	numbers_list = []
	#will hold names converted to ordered number sets

	for i in names_list:
	#takes each name

		i_list = []

		#print(i)
		#TEST

		for j in i:
		#takes each letter in name, finds it's numerical value, then puts in a list

			i_list.append( letter_to_number.main(j) )

		numbers_list.append(i_list)
		#adds list of values for each letter of a single name to the "numbers_list"

		#print(i_list)
		#TEST

	numbers_list = sorted( numbers_list )
	#sorts numbers list "alphabetically" (by comparing first number in each entry, then the next, etc. and ordering with lowest entries first

	sums_list=[]

	for i in numbers_list:
	#takes each name (currently a list of digits) and sums it into a single number

		sums_list.append( sum( i ) )

	product_sum = 0

	j = 1
	#index

	while j <= len (sums_list):
	#continues until all products have been added to sum

		product_sum += ( sums_list[j-1] * j )
		#adds product of sum of name and it's position in the list to "product_sum"

		j+=1
		#increments index j


	return product_sum



