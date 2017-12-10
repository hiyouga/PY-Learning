#max.py

x1, x2, x3 = 6, 8, 1
if x1 >= x2 and x1 >= x3:
	max1 = x1
elif x2 >= x1 and x2 >= x3:
	max1 = x2
else:
	max1 = x3
print(max1)

if x1 >= x2:
	if x1 >= x3:
		max2 = x1
	else:
		max2 = x3
else:
	if x2 >= x3:
		max2 = x2
	else:
		max2 = x3
print(max2)

max3 = x1
if x2 > max3:
	max3 = x2
if x3 > max3:
	max3 = x3
print(max3)

n = eval(input("How many numbers are there?"))
max4 = eval(input("Enter a number >> "))
for i in range(n-1):
	x = eval(input("Enter a number >> "))
	if x > max4:
		max4 = x
print("The largest value is", max4)

print(max(x1, x2, x3))