import numpy as np
import time

n = 10000

x = np.random.randn(n,n)

print("Matmul start")
a = time.time()
y = np.matmul(x, x)

#print(str(x))

print(time.time() - a)
