#ALMOST ENTIRELY COPIED FROM euler18.py


#https://projecteuler.net/problem=67
#finding max sum path through triangle
#y starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.

#Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

#NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)


def main():

	data_file = open('triangle.txt')
	#opens triangle.txt

	data = data_file.read().split()
	#creates list (data) containing all the numbers separated by commas (numbers are still considered to be strings)

	for i in range( 0, len( data )):
	#converts entries in data to numbers

		data[ i ] = int( data[ i ] )

	data_file.close()
	#closes data.txt


	num_row = 100

	for i in range (num_row-1,0,-1): #no ops needed for first row

		row_start = i * (i+1) // 2  #index for row start

		#print("row_start=",row_start)	#TEST

		#row_length = i + 1

		for j in range(0,i):
		#want to check if data[row_start+j] >= data[row_start+j+1] and add larger one to previous row

			#print("i=",i,"j=",j)	#TEST

			if data[row_start+j] >= data[row_start+j+1]:
				data[row_start+j-i] = data[row_start+j-i] + data[row_start+j]
			else:
				data[row_start+j-i] = data[row_start+j-i] + data[row_start+j+1]

	#prints desired answer
	print(data[0])

	#prints whole data as triangle
	q=0
	for k in range(0,num_row):
		#print("q=",q,"k=",k)	#TEST
		q=q+k	#TEST
		print(data[q:q+k+1])


