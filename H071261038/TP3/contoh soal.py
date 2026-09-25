# Catatan Pengeluaran

total_barang = 0

# Perulangan penjualan selama 7 hari
for i in range(1, 8):
    jumlah = int(input(f"Masukkan hari ke-{i}: "))
    total_barang = total_barang + jumlah

print(f"total barang terjual = {total_barang}")
