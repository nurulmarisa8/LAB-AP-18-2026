menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_Kopi = jumlah[0]*harga[0]
sub_Matcha = jumlah[1]*harga[1]
sub_Americano = jumlah[2]*harga[2] 

subtotal_pendapatan=(sub_Kopi,sub_Matcha,sub_Americano)
total_pendapatan = sum(subtotal_pendapatan)

BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_pendapatan-BIAYA_OPERASIONAL

total_barang_terjual = sum(jumlah)
target_tercapai = total_pendapatan>200000 and total_barang_terjual>10

print("pandapatan total:",total_pendapatan)
print("pendapatan bersih:", pendapatan_bersih)
print("hasil terget:", target_tercapai)