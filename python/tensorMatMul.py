import tensorflow as tf
import numpy as np
import time

with tf.Session() as sess:
   print("Running matrix multiplication using tensorflow")

n = 10000

x = np.random.randn(n,n)

print("Matmul start")
a = time.time()
product = tf.matmul(x, x)

print("Matmul end: " + str(time.time() - a) + (" (seconds)"))
