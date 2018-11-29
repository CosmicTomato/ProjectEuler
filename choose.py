#choose.py


#implements a choose b = a! / (b!*(a-b)!)

def main(a,b):

  #initializing
  fact=1
  divisor1=1
  divisor2=1

  #calculates top factorial
  for i in range(1,a+1):
    fact = fact * i

  #calculates bottom factorial1
  for j in range(1,b+1):
    divisor1 = divisor1 * j

  #calculates bottom factorial2
  for k in range(1,a-b+1):
    divisor2 = divisor2 * k

  #calculates answer
  ans=fact//(divisor1*divisor2)

  #returns answer
  return ans


