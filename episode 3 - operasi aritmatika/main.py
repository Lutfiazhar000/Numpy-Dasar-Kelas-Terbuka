import numpy as np

# list python
a = [1,2,3,4]
b = [5,6,7,8]

# array numpy
a_np = np.array([1,2,3,4])
b_np = np.array([5,6,7,8])

# ELEMENTWISE operation
# penjumlahan
hasil = a+b # akan menyambungkan 2 list
hasil_np = a_np+b_np # akan melakukan operasi aritmatika

# pengurangan # hasil2 = a-b # error:operasi pengurangan tidak bisa digunakan pada list
hasil2_np = a_np-b_np 

# perkalian
hasil3_np = a_np*b_np 

# pembagian
hasil4_np = a_np/b_np 

# kuadrat
hasil5_np = a_np**2
hasil6_np = b_np**2

# multidimensi array numpy
c_np = np.array(([2,4,5],[6,7,8]))
d_np = np.array(([2,7,5],[9,7,8]))

hasil7_np = c_np + d_np
hasil8_np = c_np * d_np

# display
print(hasil, "\n")
print(hasil_np, "\n")
print(hasil2_np, "\n")
print(hasil3_np, "\n")
print(hasil4_np, "\n")
print(hasil5_np, "\n")
print(hasil6_np, "\n")
print(hasil7_np, "\n")
print(hasil8_np, "\n")





# list tidak dapat melakukan operasi pengurangan,perkalian maupun pembagian