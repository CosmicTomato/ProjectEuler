#euler18.py
#https://projecteuler.net/problem=18
#finding max sum path through triangle

def main():

	data = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

	num_row=eval(input("Number of rows=? "))

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


main()
