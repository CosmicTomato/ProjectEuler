#factorial.py
#main fnc. computes the factorial of a number


def main(x):

 fact = 1 #initializing

 for i in range(x, 1, -1):

  fact = fact * i

 return fact


