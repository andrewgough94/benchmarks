import tensorflow as tf
import numpy as np
import time

with tf.Session() as sess:
   print("Running matrix multiplication using tensorflow")

n = 10000

x = np.random.randn(n,n)

#print(str(x))

a = time.time()

out = x.dot(x)

print("A: " + str(time.time() - a))

n = 10000

#x = np.random.randn(n,n)
#y = np.random.randn(n,n)
print("Matmul start")
a = time.time()
product = tf.matmul(x, x)

print("B: " + str(time.time() - a))
