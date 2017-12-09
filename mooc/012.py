#math_and_random.py

from random import *
print(random())
print(uniform(1,10))
print(randint(1,10))
print(randrange(0,10,2))
ra = [0,1,2,3,4,5,6,7,8,9]
print(choice(ra))
shuffle(ra)
print(ra)
print(sample(ra,4))
seed(10)
print(uniform(1,10))
print(uniform(1,10))
seed(10)
print(uniform(1,10))
print(uniform(1,10))
