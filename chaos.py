def main():
	print("this does stoof")
	x=eval(input("Enter a number b/w 0 & 1: "))
	y=eval(input("Enter a 2nd number b/w 0 & 1: "))
	n=eval(input("How many numbers should be printed? "))
	for i in range(n):
		x = 2.0 * x * (1-x)
		y = 2.0 * y * (1-y)
		print(x , y)
main()
