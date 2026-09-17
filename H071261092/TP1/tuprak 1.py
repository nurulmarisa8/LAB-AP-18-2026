
#data awal
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

#1. subtotal per item
sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga[1]*jumlah[1]
sub_americano = harga[2]*jumlah[2]

#2. subtotal pendapatan 
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
total_seluruh = sub_kopi + sub_matcha + sub_americano

#3. biaya operasional dan pendapatan bersih
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

#4. target tercapai
jumlah_barang = jumlah[0] + jumlah[1] + jumlah[2]
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

#tampilkan hasil

print(f"total seluruh pendapatan :{total_seluruh}")
print(f"total pendapatan bersih :{pendapatan_bersih}")
print(f"target tercapai:{target_tercapai}")
print(f"subtotal pendapatan:{subtotal_pendapatan}")