#pulls primes below one million



def main():

	f = open('primes_below_one_million.txt')

	primes=f.read().replace("'","").split(',')

	f.close()

	for i in range( 0, len( primes )):

		primes[ i ] = int( primes[ i ] )

	return primes

