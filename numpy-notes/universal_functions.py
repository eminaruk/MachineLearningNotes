import numpy as np

x = np.arange(5, 14).reshape(3,3)
np.add.reduce(x, (0,1))
y = np.zeros(3, dtype=float)

np.multiply.reduce(x, dtype=float, out=y)

print(x)
print(y)