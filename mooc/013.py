#pai.py
from random import random
from math import sqrt
from time import clock
DARTS = int(input("Input DARTS:"))
hits = 0
clock()
for i in range(1,DARTS):
	x, y = random(), random()
	dist = sqrt(x**2 + y**2)
	if dist <= 1.0:
		hits = hits + 1
pi = 4 * (hits / DARTS)
print("Pi is %s" % pi)
print("Time is %-5.5ss" % clock())