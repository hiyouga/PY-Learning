#try.py
while True:
	try:
		x = int(input("Please enter a number: "))
	except ValueError:
		raise print("Oops! That was no valid number.")