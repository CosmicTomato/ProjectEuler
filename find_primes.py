#find_primes.py
#finds a list of all primes below the desired number

def main():
	print("This function finds a list of all primes below the desired number")
	n=eval(input("Desired number=? "))
	primelist=[2]
	j=3
	for i in range (3,n,2):
		while i%j != 0 and j < (i//2+1): #only need to see if it divides up to here
			j=j+2
		if j > (i//2): #had j>(i//2+1) but it excluded some primes
			primelist.extend([i])
		j=3
	print("The primelist is: ",primelist)
main()

