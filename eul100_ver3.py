#Arranged probability

#If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

#The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

#By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.




#(x/y)((x-1)/(y-1))=1/2
#i.e. 2*x*(x-1) = y*(y-1)
#NOTE: this is ALMOST y^2 = 2x^2
#SO y roughly equals (root 2)*x


def main( y_floor, max_iter ):

	iter = 1
	sqrt2 = ( 2 ** 0.5 )
	#may need better approx. for sqrt(2)?

	y = y_floor
	#start with y_floor


	while iter < max_iter:

		x = ( y // sqrt2 ) + 1

		#need to check if 2x * (x-1) = y * ( y - 1 )
		#if candidates are correct, choose them. otherwise increment y and iteration number
		if ( 2 * ( x * ( x - 1 ) ) ) == ( y * (y - 1 ) ):
			return ( x , y )

		else:
			y += 1
			iter += 1



