#Consider quadratic Diophantine equations of the form:
#x^2 – Dy^2 = 1
#For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#It can be assumed that there are no solutions in positive integers when D is square.
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#3^2 – 2×2^2 = 1...
#9^2 – 5×4^2 = 1...
#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.




import dio_soln
#function dio_soln.main(d) finds the mininum x for which the diophantine equation has a solution
#returns solution in form [x,y]

def main(max):
#solves the stated problem for d<= max

	stored_num = [0,0,0]
	#will store d,x

	for d in range (2,max+1):

#TEST
		print (d)
#TEST

		a = dio_soln.main(d)
		#calculates min. x

		if a[0] > stored_num[1]:
		#stores d,x if x > previous largest x

			stored_num = [d,a[0],a[1]]

	return stored_num
	#returns d, x, y
