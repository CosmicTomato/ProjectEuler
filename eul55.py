#If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

#Not all numbers produce palindromes so quickly. For example,

#349 + 943 = 1292,
#1292 + 2921 = 4213
#4213 + 3124 = 7337

#That is, 349 took three iterations to arrive at a palindrome.

#Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

#Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

#How many Lychrel numbers are there below ten-thousand?




import number_palindrome
#number_palindrome.main(q) returns palindrome of q (number with digits reversed)



def check_palindrome(p):
#returns 1 if number is a palindrome, 0 if not

	if number_palindrome(p) == p:

		return 1

	else:

		return 0


def main(x):
#searches for Lychrel numbers (those that require over fifty iterations at least!) below x

	Lychrel_numbers = 0

	for i in range(1,x):

		Lychrel = 1
		#used as a check - switched to 0 if palindrome is ever found

		j = 1
		#used to count iterations

		num = i
		#new calculated number, changes with each iteration

		while j < 50 and Lychrel == 1:

			num = num + number_palindrome.main(num)
			#adds the numbers palindrome to itself

			j += 1
			#increments step number by 1

			if num == number_palindrome.main(num):
			#conditionally changes check number to 0 if a palindrome is found

				Lychrel = 0

		Lychrel_numbers += Lychrel
		#adds check number (Lychrel) to total. check is 1 if number is Lychrel, 0 if any palindrome has been found

	return Lychrel_numbers









