#The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

#How many n-digit positive integers exist which are also an nth power?



sum = 0

for i in range(1,11):

	for j in range(1,101):

		if len(str(i**j)) == j:

			sum += 1

			print (i,j,i**j)
			#TEST

print(sum)


