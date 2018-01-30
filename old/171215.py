import math
import numpy as np  
import matplotlib.pyplot as plt  
  
plt.figure(1)
ax = plt.subplot(111)
x = np.linspace(0, 100, 1000000)

r = np.sin(x) / x
ax.plot(x, r)


plt.show()