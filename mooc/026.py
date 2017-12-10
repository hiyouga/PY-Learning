#average7.py
def main():
	infile = open("026.in", 'r')
	sumn = 0.0
	count = 0
	line = infile.readline()
	while line != "":
		for xStr in line.split(","):
			sumn += eval(xStr)
			count += 1
		line = infile.readline()
	print("\nThe average of the numbers is", sumn / count)

main()