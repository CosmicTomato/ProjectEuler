#summerator.py
#sums a bunch of numbers
#prompts for number of numbers, then numbers, then sums

def main():
	n=eval(input("enter the number of numbers you want to sum: "))
	sum=0
	for i in range(n):
		print("enter the",i+1,"th number to sum: ",end='')
		number=eval(input())
		sum=sum+number
	print(sum)
main()
