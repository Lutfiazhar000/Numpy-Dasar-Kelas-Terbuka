import numpy as np

A = np.array([(2,3),(1,2)])
Y = np.array([23,14])

print(A,"\n")
print(Y,"\n")

AInv = np.linalg.inv(A)

# menyelesaikan persamaan linier
X = np.dot(AInv,Y)
print(X,"\n")

# atau dengan cara
X2 = np.linalg.solve(A,Y)
print(X2)