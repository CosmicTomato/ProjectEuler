#Finds a numbers prime factors (including duplicates, given a string of prime numbers (all prime factors of the number must be contained in the string)


#if the number cannot be factored given the inputs, this will return a blank list



def main( number, primes ):

	divisorlist = []	#will be list of all divisors

	check_prime = primes[0]	#will be holder for prime being divided out

	i = 0			#holder for index of prime being divided out

	remainder = number	#remainder will be the number as primes are divided our

	primes.extend([0])  	#adding zero at end of primes list to use for a check/stop later

	while remainder >= check_prime and check_prime !=0:	#divides out until number is factored or end of list of primes is reached

		while remainder % check_prime == 0:	#loop divides out as many copies as possible of prime, adds to divisor list

			divisorlist.extend([check_prime])
			remainder = remainder // check_prime

		i = i + 1			#increments to check next prime
		check_prime = primes[i]


	if remainder == 1:
		return divisorlist	#if factoring successful, returns divisor list

	else:
		return []		#if the number cannot be factored given the inputs, this will return a blank list




