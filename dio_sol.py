#created for use in project euler problem 66


#Consider quadratic Diophantine equations of the form:
#x^2 – Dy^2 = 1
#For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#It can be assumed that there are no solutions in positive integers when D is square.
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#3^2 – 2×2^2 = 1...
#9^2 – 5×4^2 = 1...
#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.



def find_sq(q):
#finds first q square numbers, puts them in a list

	sq_list = []

	for i in range( 1, q+1 ):

		sq_list.append( i ** 2 )

	return sq_list

def main(sq_list,d):
#finds min x for which x^2-d*y^2=1
#i.e. for which d*y^2+1 is a square number

	if d ** 0.5 == int (d ** 0.5):

		return[ 0,0 ]
	#returns 0 if d is square

	y = 1

	while y < ( 10 ** 5 ):
	#puts cap on iterations

		if ( d * (y ** 2) + 1 ) in sq_list:
		#if d*y^2+1 is square, it means a solution has been found

			x = ( d * (y ** 2) + 1 ) ** 0.5

			return [ x, y ]

		else:
		#i.e. if no solution yet

			y += 1
			#increments y











