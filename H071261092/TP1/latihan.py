
barang = ["pulpen", "buku", "pensil"]
harga = [5000, 10000, 3000]
jumlah = [2, 3, 4]

sub_pulpen = harga[0]*jumlah[0] 
sub_buku = harga[1]* jumlah[1]
sub_pensil = harga[2]*jumlah[2]

subtotal = [sub_pulpen, sub_buku, sub_pensil]
total_pendapatan = sub_pulpen + sub_buku + sub_pensil

print(f"total_pendapatan:{total_pendapatan}")
