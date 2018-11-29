#Roman numerals

#For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

#For example, it would appear that there are at least six ways of writing the number sixteen:

#IIIIIIIIIIIIIIII
#VIIIIIIIIIII
#VVIIIIII
#XIIIIII
#VVVI
#XVI

#However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

#The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

#Find the number of characters saved by writing each of these in their minimal form.

#Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.




import roman_num_to_int
import int_to_roman_num
#note: int_to_roman_num.main( x ) outputs a string of letters, separated by commas


def main():

	f = open( 'roman.txt' )
	rom_num_list = f.read().split('\n')
	f.close()
	#creates list of all the roman numerals in the text file, separated by commas

	char_diff = 0
	#will count characters saved by writing numbers in minimal form

	for rom_num in rom_num_list:

		init_len = len( list( rom_num ) )

		num_val = roman_num_to_int.main( rom_num )

		opt_num = int_to_roman_num.main( num_val )

		new_len = len( opt_num )

		char_diff += ( init_len - new_len )

	return char_diff



