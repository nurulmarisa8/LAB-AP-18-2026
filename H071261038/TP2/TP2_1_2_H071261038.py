# Soal 2
jarak = int(input("masukkan jarak pengiriman (km): "))
layanan = input("layanan express (ya/tidak): ")

# menentukan tarif dasar berdasarkan jarak
if jarak < 5:
    tarif_dasar = 10000
elif jarak <= 20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000

# ternary operator biaya tambahan express
biaya_express = 15000 if layanan == "ya" else 0

total_tarif = tarif_dasar + biaya_express
print(f"total tarif pengiriman: Rp{int(total_tarif)}")

