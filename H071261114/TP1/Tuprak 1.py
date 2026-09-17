menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]
print ("subtotal kopi susu, matcha latte, americano")
print (f"Subtotal Kopi Susu: Rp{sub_kopi}")
print(f"Subtotal Matcha Latte: Rp{sub_matcha}")
print(f"Subtotal Americano: Rp{sub_americano}")

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
print ("subtotal pendapatan keseluruhan")
print(f"List Subtotal Pendapatan: {subtotal_pendapatan}")

BIAYA_OPERASIONAL = 15000
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL
print(f"Total Seluruh Pendapatan: Rp{total_seluruh}")
print(f"Pendapatan Bersih: Rp{pendapatan_bersih}")

jumlah_barang = sum(jumlah)
target_tercapai = (total_seluruh > 200000) and (jumlah_barang > 10)
print(f"Total Barang Terjual: {jumlah_barang}")
print(f"Target Tercapai: {target_tercapai}")
