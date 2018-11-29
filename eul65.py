#Convergents of e


#The square root of 2 can be written as an infinite continued fraction.

#√2 = 1 +	
#1/
# 	2 +	
#1/
# 	 	2 +	
#1/
# 	 	 	2 +	
#1/
# 	 	 	 	2 + ...
#The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].

#It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2...
 
#Hence the sequence of the first ten convergents for √2 are:

#1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
#What is most surprising is that the important mathematical constant,
#e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

#The first ten terms in the sequence of convergents for e are:

#2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
#The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

#Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.






def main(d):
#finds the numerator and denominator of dth convergent, for d >= 3

	iter = 2
	#iteration number

	num_list = [ 2, 3 ]
	denom_list = [ 1, 1 ]
	#first two convergents are 2, 3. will continue to add new ones to lists

	while iter < d:

		iter += 1
		#increments iteration number

		if (iter % 3 ) == 0:
		#every 3 convergents, sequence has 2k term

			mult = 2 * ( iter // 3 )

		else:
		#otherwise the sequence has terms that are 1

			mult = 1

		num_list.append( ( num_list[ -1 ] * mult ) + num_list[ -2 ] )
		denom_list.append( ( denom_list[-1] * mult ) + denom_list[ -2 ] )
		#finds new denominator and numerator and appends to lists (new = old * mult + previous)


#TEST
#	print(num_list)
#	print(denom_list)
#TEST

	return('the ','d','th expansion is: ',num_list[-1],'/',denom_list[-1])


























