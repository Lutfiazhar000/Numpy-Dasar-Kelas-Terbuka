import numpy as np

a = np.array([(1,-1),(1,1)])

print(a)

# invers matrix
aInv = np.linalg.inv(a)

print(aInv)
# determinan matrix
aDet = np.linalg.det(a)
aDetInv = np.linalg.det(aInv)

print(aDet)
print(aDetInv)