from sympy import *
import symbol
import math

x = Symbol('x')
y = pow(x,-1/2) * exp(x)
print(diff(y,x))