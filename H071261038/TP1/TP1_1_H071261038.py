# Data Penjualan
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# Subtotal untuk masing-masing minuman
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah [1]
sub_americano = harga[2] * jumlah[2]

# Masukkan ketiga subtotal ke dalam list subtotal_pendapatan
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# Hitung total seluruh pendapatan bersih
Biaya_Operasional = 15000
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = total_seluruh - Biaya_Operasional

# Hitung jumlah semua barang yang terjual dan status target_tercapai
total_barang = sum(jumlah)
target_tercapai = (total_seluruh > 200000) and (total_barang > 10)

# Cetak Hasil
print("Subtotal Pendapatan  :", subtotal_pendapatan)
print("Pendapatan Bersih    : Rp", pendapatan_bersih)
print("Target Tercapai      :", target_tercapai)
