#average5.py
def main():
	infile = open("025.in", 'r')
	sumn = 0.0
	count = 0
	for line in infile:
		sumn += eval(line)
		count += 1
	print("\nThe average of the numbers is", sumn / count)

main()

'''
line = infile.readline()
while line != "":
	line = infile.readline()
'''