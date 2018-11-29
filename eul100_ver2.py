#Arranged probability

#If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

#The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

#By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.




#(x/y)((x-1)/(y-1))=1/2
#i.e. 2*x*(x-1) = y*(y-1)

def main( y_floor, max_iter ):

	iter = 1

	y = y_floor
	#start with y_floor

	z = ( y * ( y - 1 ) ) // 2
	#should evenly divide by 2


	zroot = z ** 0.5
	x_floor = int( zroot )
	#finds square root of z as floor of x

	x = x_floor
	#start with floor

	while iter < max_iter:

		#need to check if x * (x-1) = z for some y

		q = 2 * x * ( x + 1 )


		#if candidates are correct, choose them. otherwise increment x and iteration number
		if NEW CONDITION:

			return (x+1,y)

		else:

			x += 1
			iter += 1



