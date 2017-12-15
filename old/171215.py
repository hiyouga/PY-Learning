import math
import numpy as np  
import matplotlib.pyplot as plt  
  
plt.figure(1)
ax = plt.subplot(111)
x = np.linspace(-20, 20, 1000000)

r = pow(x, -1/2) * pow(math.e, -x)
ax.plot(x, r)

y = pow(abs(x), 2/3) * pow(x-2, 2)
ax.plot(x, y)

z = 1 - x + pow(pow(x, 3)/ (3+x), 1/2)
ax.plot(x, z) 

s = -2 * x + 2/5
ax.plot(x, s)

t = 0 * x
ax.plot(x, t)

plt.show()