#loop.py

words = ['cat', 'window', 'defensestrate']
for w in words:
	print(w, len(w))

for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)
print(words)

n = eval(input("How many?"))
sumn = 0.0
for i in range(n):
	x = eval(input("Enter a number >> "))
	sumn = sumn + x
print("\nThe average is", sumn / n)

i = 0
while i <= 10:
	print(i)
	i = i + 1

sum2 = 0
num = 0
while num < 20:
	num += 1
	sum2 += num
	if sum2 > 100:
		break
print("The number is", num)
print("The sum is", sum2)

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n // x)
			break
	else:#when no break and foreach complete
		print(n, 'is a prime number')

#This 'else' maybe like the 'except' in 'try-except condition'