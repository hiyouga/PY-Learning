#average2.py
def main():
	sumn = 0.0
	count = 0
	moredata = "yes"
	while moredata[0] == "y":
		x = eval(input("Enter a number >> "))
		sumn += x
		count += 1
		moredata = input("Do you have more numbers (yes or no)?")
	print("\nThe average of the numbers is", sumn / count)

main()