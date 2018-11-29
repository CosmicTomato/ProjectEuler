#file created during learning how to read/write/edit files in python

def main():

	path = '/users/Jeffrey/days.txt'

	days_file = open(path,'r')

	days_file.readlines()

	days_file.close()


def write():

	title = 'Days of the Week\n'

	path = '/users/Jeffrey/days.txt'

	days_file = open(path,'r')

	days = days_file.read()

	new_path = '/users/Jeffrey/new_days.txt'

	new_days = open(new_path,'w')

	new_days.write(title)

	print(title)

	new_days.write(days)

	print(days)

	days_file.close()

	new_days.close()




