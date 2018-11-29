#XOR decryption


#Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

#A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

#For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

#Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

#Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.



#DON'T NEED FOR PROBLEM
def num_to_bin(num_list):
#takes in a list of numbers and converts them to binary

	bin_list = []

	for i in num_list:
	#converts each number to binary, adds to list

		bin_list.append( bin( i ) )

	return bin_list





#built in functions:
#ord('A') (returns 65) converts A to a (base 10) number
#chr(65) = chr(0b1000001) (returns A) - converts 65 to an ascii character
#bin(65) (returns 0b1000001) - converts 65 to a binary number (has leading 0b to identify as binary)
#a ^ b returns a XOR b (Ex: 65 ^ 42 = 107)

def str_to_num( str ):
#converts a string to a list of numbers

	str = list( str )
	#converts str to a list of single digit strings divided by commas

	num_list = []

	for i in str:
	#converts each entry in string to number and appends to num_list

		num_list.append( ord( i ) )

	return num_list


def num_to_str( num_list ):
#reverse operation of str_to_num. converts list of numbers to a string

	str = ''
	#str starts as empty string

	for i in num_list:
	#for each number in list, finds the character corresponding to it and concatenates with string

		str += chr( i )

	return str

def XOR_with_key( num_str, key_str ):
#takes a number string and XORs it with a key of arbitrary length
#key is assumed to be string

	key = str_to_num( key_str )
	keylen = len( key )
	#converts key to a number list and gets its length to use later

	output = []

	for i in range( 0, len( num_str ) ):
	#goes through every index of number string

		output.append( num_str[ i ] ^ key[ i % keylen ] )
		#appends     number[index] XOR key[index corresponding to next character in key - loops around if key too short

	return output

def decrypt( num_str, key_str ):
#takes in a string of numbers, outputs text

	numbers = XOR_with_key( num_str, key_str )
	#XORs number string with key

	output = num_to_str( numbers )
	#converts numbers to string

	return output

def encrypt( str, key_str ):
#takes in string and key, outputs number string
#not necessary for problem

	num_str = str_to_num( str )
	#converts string to numbers

	output = XOR_with_key( num_str, key_str )
	#XORs numbers with key

	return output 



def problem():
#solves defined problem

	low_let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	#list of all lowercase letters

	cipher_file = open( 'cipher.txt' )
	#opens file

	cipher_text = cipher_file.read().replace('\n','').split(',')
	#reads data, copies to cipher_text, removes line breaks, splits into list

	for i in range( 0, len( cipher_text )):
	#converts entries in cipher_text to numbers

		cipher_text[ i ] = int( cipher_text[ i ] )

	cipher_file.close()
	#closes file

	for i in low_let:

		for j in low_let:

			for k in low_let:

				key_str = i + j + k
				#creates 3 character keystring from all lowercase latters

#TEST
				print('keystring=',key_str)
#TEST

				decrypt_text = decrypt( cipher_text, key_str )
				#tries decrypting the text using the keystring

				if 'the' in decrypt_text and 'to' in decrypt_text and 'be' in decrypt_text and 'and' in decrypt_text:
				#simple criteria to test if output is English

					print('key =',key_str)
					return decrypt_text







