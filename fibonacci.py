#fibonnaci.py
#calculates and stores the first n fibonnaci nunmbers

def main():
	sequence=[1,1]
	n=eval(input("number of fibonnaci numbers desired=? "))
	for i in range(n-2):
		sequence.extend([sequence[i]+sequence[i+1]])
	print(sequence)
main()
