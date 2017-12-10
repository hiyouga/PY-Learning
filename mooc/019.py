#quadratic5.py
import math
def main():
	print("Solve ...")
	try:
		a, b, c = input("Enter A,B,C:")
		discRoot = math.sqrt(b * b - 4 * a * c)
		root1 = (-b + discRoot) / (2 * a)
		root2 = (-b - discRoot) / (2 * a)
		print("\nThe Solutions are:", root1, root2)
	except ValueError as excObj:
		if str(excObj) == "math domain error":
			print("No Real Roots")
		else:
			print("You didn't give me the right number")
	except NameError:
		print("\nYou didn't enter three numbers")
	except TypeError:
		print("\nYour inputs were not all numbers")
	except SyntaxError:
		print("\nYour input was not in the correct form. Missing comma?")
	except:
		print("\nSomething went wrong, sorry!")

main()