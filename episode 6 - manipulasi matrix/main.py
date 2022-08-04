import numpy as np

a = np.array((
            [1,2,3],
            [4,5,6]
            ))

# shape
print(f"matrix a memiliki ukuran {a.shape}")
print(a)

# transpose
print("transpose dari matrix a:")
print(a.transpose())
print(np.transpose(a))
print(a.T)

# flatten (merubah menjadi vextor baris)
print("faltter dari matrix a:")
print(a.ravel())
print(np.ravel(a))

# reshape matrix
print("reshape dari martrix a:")
print(a.reshape(3,2))

# resize matrix
print("resize dari matrix a:")
print(a.resize(3,2)) # akan merubah nilai semula a