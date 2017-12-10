#quadratic.py

import math
def main():
	print("Solve quedratic\n")
	a, b, c = eval(input("Please enter A,B,C"))
	delta = b * b - 4 * a * c
	if delta < 0:
		print("The equation has no real roots")
	else:
		discRoot = math.sqrt(delta)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print("\nThe Solutions are:", root1, root2)
main()