#Odd period square roots
#All square roots are periodic when written as continued fractions and can be written in the form:

#√N = a0 +	
#1/
# 	a1 +	
#1/
# 	 	a2 +	
#1/
# 	 	 	a3 + ...

#for sqrt(23):
#It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

#The first ten continued fraction representations of (irrational) square roots are:

#√2=[1;(2)], period=1
#√3=[1;(1,2)], period=2
#√5=[2;(4)], period=1
#√6=[2;(2,4)], period=2
#√7=[2;(1,1,1,4)], period=4
#√8=[2;(1,4)], period=2
#√10=[3;(6)], period=1
#√11=[3;(3,6)], period=2
#√12= [3;(2,6)], period=2
#√13=[3;(1,1,1,1,6)], period=5

#Exactly four continued fractions, for N ≤ 13, have an odd period.

#How many continued fractions for N ≤ 10000 have an odd period?




def find_series(d):
#finds series corresponding to continued fraction expansion of sqrt(d)

	series = []
	#will hold desired series

	rough_sqrt = d ** 0.5
	#calculates square root using pythons built-in math

	a = int (d ** 0.5)
	#gives int floor (sqrt(d)=a+sqrt(d)-a)

	if rough_sqrt == a:
	#returns empty list if d is square

		return series

	denom = d - (a ** 2)
	#calculates first denominator (d - a^2)

	#TEST
	#print('denom=',denom)

	new_series_num = (a + a) // denom
	#calculates new number to be added to series. pulls out as large an integer as possible to get numerator as close to sqrt(d) - a without subtracting too much

	series.append( new_series_num )
	#adds number to series

	num = (-1)*(a - (new_series_num * denom))
	#subtracts out the integer that is pulled out (times the denominator) to calculate the new numerator number

	#TEST
	#print('num=',num)

	while denom != 1:
	#loop continues until denominator is 1 (i.e. cycle has been completed)

		denom = (d - (num ** 2)) // denom
		#calculates the new denominator

		#TEST
		#print('denom=',denom)

		new_series_num = (num + a) // denom
		#calculates new number to be added to series. pulls out as large an integer as possible to get numerator as close to sqrt(d) - a without subtracting too much

		series.append( new_series_num )
		#adds number to series

		num = (-1)*(num - (new_series_num * denom))
		#subtracts out the integer that is pulled out (times the denominator) to calculate the new numerator number

		#TEST
		#print('num=',num)

	return series


def main(n):
#finds number of continued fractions for d<=n which have an odd period

	f = 0
	#will count number of fractions

	for d in range(2,n+1):
	#iterates through d from 2 to n

		a = find_series(d)
		#uses find series function defined above

		if (len(a) % 2) == 1:
		#checks if continued fraction for d has an odd period and adds one to f if it does

			f += 1

	return f

