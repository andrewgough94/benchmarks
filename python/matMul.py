import numpy as np
import time

n = 10000

x = np.random.randn(n,n)

#print(str(x))

a = time.time()

x = x.dot(x)

print(time.time() - a)
