#Anagramic squares

#By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

#What is the largest square number formed by any member of such a pair?

#NOTE: All anagrams formed must be contained in the given text file.




import letter_to_number
#letter_to_number.main(x) returns numerical value of the letter x



def main():

	f=open('words.txt')
	words_list=f.read().replace('"','').split(',')
	f.close()
	#creates list of all words in file. they are all uppercase and are separated by commas


	words_sets = []
	for i in range( 0 , len( words_list ) ):
		words_sets.append( [ set( words_list[ i ] ) , words_list[ i ] ] )
	#creates list that holds sets of all words in list (as well as all words in list)

	just_sets = []
	for i in range( 0 , len( words_sets ) ):
		just_sets.append( words_sets[ i ][ 0 ] )
	#creates list that holds just the sets of all words in list

	pruned_words = []
	for i in range( 0 , len( words_sets ) ):
		if just_sets.count( words_sets[ i ][ 0 ] ) >= 2:
			pruned_words.append( words_sets[ i ][ 1 ] )
	#if duplicate, then add words to pruned words

#IMPORTANT: pruned_words represents all words that are part share all of their letters with at least one other word in the list
#(there are 295 words in the pruned_words list)
#NOTE: these words aren't necessarily part of an anagram pair, as there could be shorter words that share all of their letters

#TEST
	print('pruned_words=',pruned_words)
#TEST

#TEST
	word_lengths = []
	for i in pruned_words:
		word_lengths.append( len( i ) )
#TEST
#RESULT: MAX length of words with anagrams is 14
#sqrt(10^14) = 10^7
#i.e. 10^7 is the first number to have a square with more than 14 digits



		return pruned_words








