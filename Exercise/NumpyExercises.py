# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 13:04:05 2021

@author: oscbr226
"""

import numpy as np 

#Numpy exercise A
exerciseA = np.zeros(10)
exerciseA[4] = 1

#Numpy exercise B
exerciseB = np.array(range(10,50))

#Numpy Exercise C
exerciseC = exerciseB.copy()
exerciseC = np.flip(exerciseC)

#Numpy Exercise D
exerciseD = np.random.randint(9, size=(3,3))

#Numpy Exercise E
exerciseE = np.array([1,2,0,0,4,0])
nonZero = np.where(exerciseE != 0)
nonZeroIndices = nonZero[0]

#Numpy Exercise F
exerciseF = np.random.random(30)
avgVal = np.mean(exerciseF)

#Numpy Exercise G
exerciseG = np.ones([3,3])
exerciseG[1,1] = 0
# print(exerciseG)

#Numpy Exercise H
exerciseH = np.zeros((8,8))
exerciseH[1::2,::2] = 1
exerciseH[::2,1::2] = 1
#print(exerciseH)

#Numpy Exercises I
arr = [[0,1],[1,0]]
repit = (4,4)
exerciseI = np.tile(arr, repit)
#print(exerciseI)
# print(np.shape(exerciseI))

#Numpy Exercise J
exerciseJ = np.arange(11)
exerciseJ[3:9] -= 2*exerciseJ[3:9]
# print(exerciseJ)

#Numpy Exercise K
exerciseK = np.random.random(10)
# print(exerciseK)
exerciseK = np.sort(exerciseK)
# print(exerciseK)

#Numpy Exercise L
randVecA = np.random.randint(0,2,5)
randVecB = np.random.randint(0,2,5)
equal = np.equal(randVecA, randVecB)
equal2 = randVecA == randVecB
# print(equal)
# print(equal2)

#Numpy Exercise M
exerciseM = np.arange(10, dtype=np.int32)
# print(exerciseM.dtype)
exerciseM = exerciseM.astype('float32')
# print(exerciseM.dtype)

#Numpy Exercise N 
arrayA = np.arange(9).reshape(3,3)
arrayB = arrayA + 1
arrayC = np.dot(arrayA,arrayB)
arrayD = np.diag(arrayC)
arrayE = arrayC[range(3),range(3)]
print(arrayD)
print(arrayE)



