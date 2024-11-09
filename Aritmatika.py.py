import pandas as pd

a = pd.DataFrame({'A': [5, 4, 7], 'B': [6, 8, 9]})
b = pd.DataFrame({'A': [1, 3, 5], 'B': [15, 22, 13]})

hasil_penjumlahan = a + b
print("Hasil penjumlahan:\n", hasil_penjumlahan)

hasil_pengurangan = a - b
print("\nHasil pengurangan:\n", hasil_pengurangan)

hasil_perkalian = a * b
print("\nHasil perkalian:\n", hasil_perkalian)

hasil_pembagian = a / b
print("\nHasil pembagian:\n", hasil_pembagian)


