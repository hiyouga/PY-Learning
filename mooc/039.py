#filecopy.py
def main():
	infile = open("039.in", "r")
	outfile = open("039.out", "w")

	countLines = countChars = 0
	for line in infile:
		countLines += 1
		countChars += len(line)
		outfile.write(line)
	print(countLines, " lines and ", countChars, " chars copied")

	infile.close()
	outfile.close()
main()