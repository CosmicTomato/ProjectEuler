#given a number, finds the circular rotations of it

def main(x):

	rot_list = [x]

	num_str = str(x)	#creates a string from x

	for i in range(1,len(num_str)):

		num_str = num_str[1:] + num_str[0]

		rot_list.append(int(num_str))

	return rot_list

