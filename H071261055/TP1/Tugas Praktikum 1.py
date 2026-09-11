menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi_susu = harga[0] * jumlah[0]
sub_matcha_latte = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi_susu, sub_matcha_latte, sub_americano]

total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

jumlah_barang = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

print(f"subtotal pendapatan kopi susu: Rp{sub_kopi_susu}")
print(f"subtotal pendapatan matcha latte: Rp{sub_matcha_latte}")
print(f"subtotal pendapatan americano: Rp{sub_americano}")
print(f"pendapatan bersih: Rp{pendapatan_bersih}")
print(f"hasil target tercapai: {target_tercapai}")