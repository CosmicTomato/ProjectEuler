#The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.




import number_permutations
#number_permutations.main(x) returns all the permutations of x in a list


def is_cube(x):
#dirty method to check if a number is a cube
#returns 1 if number is a cube (within tolerance), otherwise returns 0

	tolerance = 10 ** (-12)

	cube_root = x ** (1/3)

	if abs(cube_root)>abs(round(cube_root))-tolerance and abs(cube_root)<abs(round(cube_root))+tolerance:

		return 1

	else:

		return 0

def main(p):
#finds first number with p cube permutations

	i = 100
	# need to start search with at least 3-digit number

	desired_number = 0
	#will hold number once found, used as check in while loop

	while desired_number == 0:
	#loop continues until suitable number found

		#TEST
		print(i)

		q = i ** 3
		#finds cube of number

		cube_permutations = 0
		#will be used to count number of permutations that are cubes

		permute_list = number_permutations.main(q)
		#gets the permutations of i^3

		cube_list = []
		#for testing purposes, stores list of cube permutations

		for j in permute_list:
		#checks if j is a cube, if it is adds one to the number of found cube permutations

			cube_num = is_cube(j)

			cube_permutations += cube_num

			if cube_num == 1:
			#for testing purposes, stores list of cube permutations

				cube_list.append(j)

		if cube_permutations == p:
		#defines required criteria

			desired_number = q

		else:

			i += 1
			#increments i if desired number has not been found

	return [i,desired_number,cube_list]


