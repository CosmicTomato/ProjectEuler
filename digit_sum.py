#finds the sum of the digits of a number

def main(x):

	sum = 0

	for i in str(x):

		sum = sum + int(i)

	return sum


