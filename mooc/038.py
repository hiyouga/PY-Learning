#file.py
def main():
	fname = input("Enter filename:")
	infile = open(fname, "r")
	data = infile.read()
	print(data)
main()
'''
universal framework:
file = open(filename, "r")
for line in file.readlines():
	#...
file.close()
OR
file = open(filename, "r")
for line in file:
	#...
file.close()
'''