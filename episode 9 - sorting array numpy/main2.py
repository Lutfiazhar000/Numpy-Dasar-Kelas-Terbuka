import numpy as np

a = np.floor(np.random.randn(2,2)*10)

# display
print(a)
print(f"nilai max dari a adalah {a.max()}")
print(f"nilai min dari a adalah {a.min()}")
print(f"nilai max dari a berada di posisi ke {a.argmax()}")
print(f"nilai min dari a berada di posisi ke {a.argmin()}")
print("\n")

print("mengurutkan nilai a")
print(np.sort(a))
print(np.argsort(a))