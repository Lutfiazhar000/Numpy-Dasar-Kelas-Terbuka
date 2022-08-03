import numpy as np

a = np.array(([1,2],
            [3,4]))

b = np.ones((2,2))

c = np.dot(a,b) # perkalian matrix
c2 = a.dot(b) # OOP python

# display
print(f"matrix a:")
print(a)
print(f"matrix b:")
print(b)
print("hasil perkalian matrix a dan b:")
print(c)
print(c2)