#average4.py
def main():
	sumn = 0.0
	count = 0
	xStr = input("Enter a number (<Enter> to quit) >> ")
	while xStr != "":
		x = eval(xStr)
		sumn += x
		count += 1
		xStr = input("Enter a number (<Enter> to quit) >> ")
	print("\nThe average of the numbers is:", sumn / count)

main()