import numpy as np

# membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[4,5,6]), dtype = float)

# membuat array dengan function
def kuadrat(baris,kolom):
    return kolom**2

def jumlah(baris,kolom):
    return (kolom + baris)

b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (5,5), dtype = float)

# membuat array dengan iterable
iterable = (x*2 for x in range(5))

d = np.fromiter(iterable, dtype = int)

# multitype array
dtipe = [('nama','S225'),('tinggi',int)]

data = [
    ('henri', 130),
    ('ruslan', 145),
    ('yono', 160)
]

e = np.array(data, dtype = dtipe)

# display
print(a, "\n")
print(b, "\n")
print(c, "\n")
print(d, "\n")
print(e, "\n")