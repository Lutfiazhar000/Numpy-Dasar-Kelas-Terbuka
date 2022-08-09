import numpy as np

a = np.array([1,3])
b = np.array([3,0])

# dot
c = np.dot(a,b)

# cross
a2 = np.array([1,2,0])
b2 = np.array([2,1,0])

c2 = np.cross(a2,b2)
c3 = np.cross(b2,a2)

# display
print(c)
print(c2)
print(c3)