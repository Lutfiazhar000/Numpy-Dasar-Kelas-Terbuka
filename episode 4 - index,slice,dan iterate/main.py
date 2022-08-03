import numpy as np

a = np.arange(10)**2

# display
'''indexing'''
print(a)
print(f"elemen 1 dari a adalah {a[0]}")
print(f"elemen 7 dari a adalah {a[6]}")
print(f"elemen terakhir dari a adalah {a[-1]}")
print("\n")

'''slicing'''
print(f"elemen dari 1-4 adalah{a[1:4]}")
print(f"elemen dari 4-akhir adalah{a[4:]}")
print(f"elemen dari awal-5 adalah{a[:5]}")
print("\n")

'''iterasi'''
for i in a:
    print("value = ",i)
