#The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.



def main(p):
#finds first number with p cube permutations

	i = 1
	#iteration number holder

	desired_number = 0
	#will hold number once found, used as check in while loop

	sorted_cube_list = [0]
	#will store cubes sorted by digits

	i_list = []
	#will store iteration numbers

	while desired_number == 0:
        #loop continues until suitable number found

		q = i ** 3
		#finds cube of number

		sorted_cube=sorted(str(q))
		#computes sorted list of form ['x','y','z'] where x,y,z are digits of q

		sorted_cube_list.append(sorted_cube)	
		#stores number that was cubed's sorted, ordered digits

		if sorted_cube_list.count(sorted_cube) == p:
		#defines required criteria (checks if number of cubes with same digits = p)

			desired_number = q

			desired_index = sorted_cube_list.index(sorted_cube)

		else:

			i += 1
			#increments i if desired number has not been found

	return [i,desired_number,desired_index]






