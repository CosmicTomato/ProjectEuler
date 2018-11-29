#prime_factors.py
#finds the prime factorization of a number

#mostly copied from euler3_ver2.py

def main(integer):
	
	#initializing variables
	integer=int(integer)
	n=integer
	primelist=[2]
	divisorlist=[]
	i=3
	j=3

	#loop continues to work while checking for divisors < (n//2+1)
	#n gets reduced by later loops so should reduce number of primes necessary to search for
	while primelist[-1]<(n//2+1):

		#loop divides out any number of factors for last prime in list and adds to divisor list
		while n%primelist[-1]==0:
			n=n/primelist[-1]
			divisorlist.extend([primelist[-1]])

		#checks if next highest odd number is prime & adds it to prime list if it is
		while i%j != 0 and j < (i//2+1): #only need to see if it divides up to here
			j=j+2
		if j > (i//2):
			primelist.extend([i])
		j=3
		i=i+2

	#switches n to an integer
	n=int(n)

	#adds n to the divisor list if it is greater than or equal to the largest divisor found so far OR IF IT IS THE ONLY DIVISOR SO FAR (I.E. n IS PRIME!)
	if divisorlist==[]:
		divisorlist.extend([n])
	elif n>=divisorlist[-1]:
		divisorlist.extend([n])

	return divisorlist	#outputs divisorlist



