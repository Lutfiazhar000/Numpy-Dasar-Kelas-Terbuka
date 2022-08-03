import numpy as np

# membuat vector
a = np.array([2,3,4,5,6])
b = np.array([1.2,3,5,4.0,8,9])

# membuat vector dengan range
c = np.arange(1,27,3) # .arrange(batasBawah,batasAtas,step)

# membuat vector dengan linspace
d = np.linspace(1,10,4) # membagi angka dengan range yg sama

# membuat array multidimensi
e = np.array([(1,2,3),(4,5,6)])

# membuat matrix dgn nilai nol
f = np.zeros((4,4))

# membuat matrix dgn nilai satu
g = np.ones((4,4))

# membuat matrix identitas
h = np.identity(5)
h1 = np.eye(5)

# display
print(a,"\n")
print(b, "\n")
print(c, "\n")
print(d, "\n")
print(e, "\n")
print(f, "\n")
print(g, "\n")
print(h, "\n")
print(h1, "\n")