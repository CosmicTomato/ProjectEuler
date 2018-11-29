#check_prime.py
#checks if a number is prime
#if prime, returns 1, if not prime, returns 0
#should probably be improved in future to be faster
#largely adapted from find_primes_below.py and find_primes.py

#imports math to use sqrt func later
import math

def main(n):

  #checks special case of if n=2
  if n==2:
    return 1

  #checks if n even, if it is returns 0 (not prime)
  elif n%2 == 0:
    return 0

  else:
    sqrtn=math.sqrt(n) #finds square root of n (only need to see if divisible by numbers up to here!)

    #initializing
    i=3

    #want to check if numbers up to sqrtn divide n
    while n%i != 0 and i <= sqrtn:

      #adds 2 to i as long as the last value of i did not (evenly) divide n
      i=i+2

    #returns 1 if n prime
    if i > sqrtn:
      return 1

    #returns 0 if n not prime
    else:
      return 0


