import os

output = open('temp.mp4', 'wb')

for i in range(49):
	fname = "1ad5af8ea9bd7503595f4540a08fbcf1.{:03d}.tdl".format(i)
	fopen = open(fname, 'rb')
	output.write(fopen.read())
	fopen.close()

output.close()