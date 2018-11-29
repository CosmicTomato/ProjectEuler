#euler9.py
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which  a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000
#This program finds (a,b,c)

def main():

	for c in range (1,500):
		a=999-c
		b=1
		while a*a + b*b != c*c and a>0:
			a=a-1
			b=b+1
		if a*a + b*b == c*c:
			print("The triplet (a,b,c) is:",a,b,c)


#PROGRAM IS DIRTY BUT GETS ANSWER


main()
