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





#based on wikipedia article (https://en.wikipedia.org/wiki/Pell's_equation), solution must be x,y=a,b when a/b is in the convergent series for the square root of D
#thus, just need to find fractions in convergent series for D, then check if they are solutions.


#Somewhat adapted from eul64 ("Odd period square roots"), find_series function
import eul64
#eul64.find_series(d) finds the numbers that go into the convergent series of d (but not the relevant fractions)


def main(d):
#finds min x for which x^2-d*y^2=1
#i.e. for which d*y^2+1 is a square number

	convergent_series = eul64.find_series(d)
	#eul64.find_series(d) finds the numbers that go into the convergent series of d (but not the relevant fractions)

	rough_sqrt = d ** 0.5
	#calculates square root using pythons built-in math

	a = int (d ** 0.5)
	#gives int floor (sqrt(d)=a+sqrt(d)-a)

	if rough_sqrt == a:
	#returns empty list if d is square

		return[ 0,0 ]	
		#returns 0 if d is square

	num_list = [a]
	denom_list = [1]
	#will hold series (first denominator is always 1)


	x = num_list[ -1 ]
	y = denom_list[ -1 ]
	if ( (x ** 2) - ( d * (y ** 2) ) ) == 1:
		return [ x, y ]
	#checks if first numbers are answer

	iter = 1
	#counts number of iterations

	len_ser = len( convergent_series )
	#finds length of convergent series to use in loop

	denom_list.append( convergent_series[ 0 ] )
	#finds new denominator

	num_list.append( (convergent_series[ 0 ] * num_list[ 0 ]) + 1 )

	while iter < ( 10 ** 3 ):
	#puts cap on iterations

		x = num_list[ -1 ]
		y = denom_list[ -1 ]


		if ( (x ** 2) - ( d * (y ** 2) ) ) == 1:

			return [ x, y ]

		mult = convergent_series[ iter % len_ser ]
		#pulls next number from convergent series (wraps around, since convergent series may be short)

		denom_list.append( denom_list[-1] * mult + denom_list[-2] )
		#finds new denominator

		num_list.append( num_list[-1] * mult + num_list[-2] )
		#finds new numerator

		iter += 1
		#increments the iteration number

#TEST
#		print(num_list)
#		print(denom_list)
#TEST






