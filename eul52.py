#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.



def main():

	desired_number = 0
	i = 1

	while desired_number == 0:

		if set(str(i))==set(str(2*i))==set(str(3*i))==set(str(4*i))==set(str(5*i))==set(str(6*i)):

			desired_number = i

		i = i + 1

	return desired_number








