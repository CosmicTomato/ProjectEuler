#Cube digit pairs


#Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.

#For example, the square number 64 could be formed:

#In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

#For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.

#However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.

#In determining a distinct arrangement we are interested in the digits on each cube, not the order.

#{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
#{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

#But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.

#How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?




#squares_list = [ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 ]
#note: 6 is equivalent to 9, 19 is equivalent to 16, 39 is equivalent to 36, 46 is equivalent to 49, 94 is equivalent to 64
#NOTE: IF CUBE HAS 6 OR 9 ON IT, IT ACTS AS IF IT HAS BOTH ON IT


NOTES:
#at least one cube needs 0,1,2,3,4,5,6,8 on it, since no 7's appear in squares_list and 6 is equivalent to 9
#CONCLUSION:
#just pretend 9 doesn't exist, then count ways you can replace 6 with 9
#squares_list = [ 1 , 4 , 6 , 16 , 25 , 36 , 46 , 64 , 81 ]

#need [ 0,6,8 ] and [ 1,4,6 ] on opposite dice -> forms 01,04,06,16,46,64,81
#(missing 25, 36)
#also need [ 2 ] and [ 5 ] on opposite dice as well as to place [3] on either die


import copy


def main():

	squares_list = [ 1 , 4 , 6 , 16 , 25 , 36 , 46 , 64 , 81 ]
	dice = [ [ 0 , 6 , 8 , 2 ] , [ 1 , 4 , 6 , 5 ] ]
	orig_dice = copy.deepcopy( dice )

	#can reverse 2 and 5 -> doubles number of combinations
	#can switch each 6 with 9 -> quadruples number of combinations
	#must still put 3 in one die

	#for first dice, assume 3 on die -> last slot can be 1,4,5,7,9  
	#if last slot 9, can switch with the 6 on the same die (not with the 6/9 on the other die since that would make the first die not have 6 unique numbers
	#so, 6 combinations
	#2nd die chooses 2 from 2,3,7,8,9
	#12 ways to choose without 9, 8 ways to choose with 9 - multiply by
!!!	#WHAT IF 6,9 on both dice?

	#assume 3 on 2nd die ->

