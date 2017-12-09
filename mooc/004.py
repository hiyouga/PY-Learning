#TempConvert_loop.py
for i in range(3):
	val = input("Input the temp:(32C)")
	if val[-1] in ['C','c']:
		f = 1.8 * float(val[0:-1]) + 32
		print("Converted temp is: %.2fF"%f)
	elif val[-1] in ['F','f']:
		c = (float(val[0:-1]) - 32) / 1.8
		print("Converted temp is: %.2fC"%c)
	else:
		print("Wrong input")