#quadratic2.py

import math
def main():
	print("Find the solutions\n")
	a, b, c = eval(input("Enter the A,B,C: "))
	delta = b * b - 4 * a * c
	if a == 0:
		x = -b / c
		print("\nThere is an solution", x)
	elif delta < 0:
		print("\nThe equation has no real roots")
	elif delta == 0:
		x = -b / (2 * a)
		print("\nThere is a double root at", x)
	else:
		discRoot = math.sqrt(delta)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print("\nThe Solutions are:", root1, root2)

main()