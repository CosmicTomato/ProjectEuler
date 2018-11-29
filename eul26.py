###PROBLEM 26: Reciprocal Cycles

#problem:
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given
#    1/2        =       0.5
#    1/3        =       0.(3)
#    1/4        =       0.25
#    1/5        =       0.2
#    1/6        =       0.1(6)
#    1/7        =       0.(142857)
#    1/8        =       0.125
#    1/9        =       0.(1)
#    1/10       =       0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


#initializing
longest_cycle=0
stored=0

#want to check all numbers d<1000
#for d in range(2,1000):


def find_decimals(x): #finds decimals of 1/x

	d = x

	#initiating variables
	rem = 1
	decimals=[]

	while rem!=0 and len(decimals)<2000:	#if rem==0, end cycle. arbitrarily ends after 2000 decimals for infinite repeats

		decimals.append((10*rem)//d)

		rem = (10*rem) % d

	decimals.append(rem//d)


	return decimals


def find_length_repeats(q):

	max_search = 1000-1		 #searches for repeats with a max length of 999, can be modified

	#initiating variables
	i = 3 #needed to make large numbers work
	repeat_length = 0

	while repeat_length == 0 and i <= max_search:	 #increments until either the length of the repeat is found or no repeat is found less than max_search in length

		if q[0:i] == q[i:2*i]:
			repeat_length = i

		elif q[1:i+1] == q[i+1:2*i+1]:
			repeat_length = i

		elif q[1:i+2] == q[i+2:2*i+2]:
			repeat_length = i
		else:
			i = i+1

	return repeat_length


def main(m): 	#solves described problem up to m (m=1000 in description)

	#initializing variables
	max_repeat_length = 0
	stored_number = 0
	i = 2

	while i <= m:

		dec = find_decimals(i)
		repeat_length = find_length_repeats(dec)

		if repeat_length > max_repeat_length:

			max_repeat_length = repeat_length
			stored_number = i

		i = i+1

	print ('stored number =',stored_number)
	print ('repeat length=',max_repeat_length)
 


