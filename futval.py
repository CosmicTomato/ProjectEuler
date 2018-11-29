#futval.py
#computes future value of investment

def main():
	principal=eval(input("principal=? "))
	apr=eval(input("apr=? "))
	years=eval(input("years=? "))
	annual=eval(input("annual investment=? "))
	for i in range(years):
		principal=principal*(1+apr)+annual
	print('future value= ',principal)
main()

