#lcm.py
#finds the least common multiple of two numbers
#gets prime factorization of each number, adds prime factors together in a list, then tries to reduce by any shared factors and checks if number still divisble by both

def main(a,b):

	#imports prime_factors.py and gets the prime factor lists
	import prime_factors
	afactors=prime_factors.main(a)
	bfactors=prime_factors.main(b)
	allfactors=afactors+bfactors

	#finds shared factors and puts in list
	sharedfactors=list(set(afactors) & set(bfactors))

	#test-number starts as product of all factors (i.e. the product of both numbers)
	test=a*b

	#tries to reduce test by all shared factors
	for j in sharedfactors:
		while test%a == 0 and test%b == 0: #reduces as long as number is divisible by both
			test = test / j
		test = test * j		#multiplies back the extra factor that gets divided out by the previous loop

	lcm=int(test)

	return lcm	#outputs lcm


