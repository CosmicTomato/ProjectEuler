#try #3

#designed for help on project euler problem 66:

#Consider quadratic Diophantine equations of the form:
#x^2 – Dy^2 = 1
#For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#It can be assumed that there are no solutions in positive integers when D is square.
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#3^2 – 2×2^2 = 1...
#9^2 – 5×4^2 = 1...
#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.



def find_sqrt(q):
#attempts to find integer square root of q, returns 0 if none found

	search_cap = int ( q ** 0.5 ) +1
	# puts cap on search based on approximate square root calculation

	y = 1

	while y ** 2 != q and y < search_cap:
	#keeps incrementing y until solution found or search is exhausted

		y+=1

	if y == search_cap:
	#returns 0 if no square root found

		return 0

	else:

		return y


def main(d):
#finds min x for which x^2-d*y^2=1

	if d ** 0.5 == int (d ** 0.5):
		return [0,0]
	#returns 0 if d is square

	x = 2
	left_side = (x ** 2) - 1
	#initializing variablaes
	#want x^2-1 = d*(y^2)

	x_cap = 10 ** 9
	#arbitrary cap on x to keep program from hanging

	#if solution exists, there should be a y that satisfies d*y^2 = x^2 - 1
	#i.e. (x^2-1)/d should be a square number

	pot_y = find_sqrt( (x ** 2 -1) / d)
	#calculates what y would be if solution is correct, makes sure it is an integer

	right_side = d * (pot_y ** 2)

	while left_side != right_side and x < x_cap:
	#continues search until answer is found, also put arbitrary cap on x

		#####TEST
		#if abs(left_side - right_side) < 10:
		#print (abs(left_side - right_side),x,pot_y)

		x += 1
		left_side = (x ** 2) - 1
		#increments x and recalcs

		while (left_side % d) != 0:
		#at bare bones, need (x^2-1)/d to be an integer

			x += 1
			left_side = (x ** 2) - 1
			#increments x and recalcs

		#pot_y = find_sqrt( (x ** 2 - 1) / d)
		pot_y = int((left_side//d) ** 0.5)

		right_side = d * (pot_y ** 2)
		#finds new pot_y and recalcs right side of equation



	return [x,pot_y]




