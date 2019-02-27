from numpy import *
import numpy as np
mod = np.array([[1000000009, 1000000009],[1000000009, 1000000009]])
a = np.array([[1, 1],[1, 0]])
n = int(input()) 
res = np.array([[1, 0],[0, 1]])
while n > 0:
	if n & 1 == 1:
		res = np.dot(res, a)
		res = res % mod
	a = np.dot(a, a)
	a = a % mod
	n = n >> 1
print(res[0][1])