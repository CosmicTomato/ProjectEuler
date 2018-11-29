#pi_approx.py
#approximates pi with n term finite sequence 4/1-4/3+4/5-4/7...

def main():
	n=eval(input("desired number of terms in sequence=? "))
	approx=0
	for i in range(n):
		approx=approx+4*((-1)**i)/(2*i+1)
	print("approx=",approx)
	import math
	print("absolute error=",abs(math.pi-approx))
main()
