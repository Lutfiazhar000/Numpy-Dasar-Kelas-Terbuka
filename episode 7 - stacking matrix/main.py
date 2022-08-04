import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

matrixA = np.zeros((2,3))
matrixB = np.ones((2,3))

# stacking matrix / menumpuk matrix

c = np.hstack((a,b)) # menumpuk secara horizontal
d = np.vstack((a,b)) # menumpuk secara vertikal

matrixC = np.hstack((matrixA,matrixB))
matrixD = np.vstack((matrixA,matrixB))

# display
print(c, "\n")
print(d, "\n")
print(matrixC, "\n")
print(matrixD, "\n")