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




def main(d):
#finds min x for which x^2-d*y^2=1

	if d ** 0.5 == int (d ** 0.5):
		return 0
	#returns 0 if d is square

	x = 2
	left_side = (x ** 2) - 1
	#initializing variables
	#want x^2-1 = d*(y^2)

	y_floor = int ( int((left_side) / d)  ** 0.5 ) - 1
	#if solution exists, there should be a y that satisfies y^2 = x^2 - 1
	y_mid = y_floor + 1
	y_cap = y_floor + 2

	right_side_floor = (d * y_floor ** 2)
	right_side_mid = (d * y_mid ** 2)
	right_side_cap = (d * y_cap ** 2)

	check = 0
	#switches when solution found

	while check == 0 and x < 10 ** 7:
	#searches until solution is found, put arbitrary cap so it doesn't hang forever

		if left_side == right_side_floor or left_side == right_side_mid or left_side == right_side_cap:

			check = 1

		else:

			x += 1
			left_side = (x ** 2) - 1
			y_floor = int ( int((left_side) / d)  ** 0.5) - 1
			y_mid = y_floor + 1
			y_cap = y_floor + 2
			right_side_floor = (d * y_floor ** 2)
			right_side_mid = (d * y_mid ** 2)
			right_side_cap = (d * y_cap ** 2)
			#increments x and relcalcs values

	return x




