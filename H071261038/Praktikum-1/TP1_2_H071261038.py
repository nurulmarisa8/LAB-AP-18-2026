# Data Penjualan
barang = ["Pulpen", "Buku", "Pensil"]
harga = [5000, 10000, 3000]
jumlah = [2, 3, 4]

# Hitung subtotal Pulpen
sub_pulpen  = harga[0] * jumlah [0]
sub_buku    = harga [1] * jumlah [1]
sub_pensil  = harga [2] * jumlah [2]

# Masukkan ketiga subtotal ke dalam list subtotal
subtotal = [sub_pulpen, sub_buku, sub_pensil]

# Hitung total pendapatan
total_seluruh = sum(subtotal)

# Cetak Hasil
print("subtotal  :", subtotal)
print(total_seluruh)