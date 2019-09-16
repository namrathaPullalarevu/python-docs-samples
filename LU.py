import pprint

import scipy

import scipy.linalg   # SciPy Linear Algebra Library

import numpy as np


a = np.matrix([ [1, 2, 3], [2, 3, 4], [1, 2, 5] ])

k = scipy.array([ [8, 2, 9], [4, 9, 4], [6, 7, 9] ])

#print("Secret key is ")

#print(k)

P, L, U = scipy.linalg.lu(k)


#print ("A:")

#pprint.pprint(k)


#print( "P:")

#pprint.pprint(P)


#print ("L:")

#pprint.pprint(L)


#print ("U:")

#pprint.pprint(U)


