import pandas as pd

data_menu = {
    'Harga': [19000, 20000, 20000, 13000, 11000, 30000, 19000, 50000, 40000, 25000]
}

menu_df = pd.DataFrame(data_menu, index=[
    'Ayam Goreng', 'Ayam Geprek', 'Gulai Bebek', 'Ayam Bakar', 'Ayam Balado', 
    'Soto Ayam', 'Ayam Strawberry', 'Nasi Padang', 'Rendang', 'Mie ayam'
])

hasil_5_teratas = menu_df.head(5)
hasil_5_terbawah = menu_df.tail(5)

print("5 Teratas:\n", hasil_5_teratas)
print("\n5 Terbawah:\n", hasil_5_terbawah)


