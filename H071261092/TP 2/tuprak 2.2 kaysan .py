jarak = float(input("Masukkan jarak pengiriman (km) : "))
express = input("layanan express (ya/tidak): ")

if jarak < 5 and jarak > 0:
    tarif_dasar = 10000
elif jarak > 5 and jarak < 20:
    tarif_dasar = 20000
elif jarak > 20:
    tarif_dasar = 35000

biaya_express = 15000 if express == "ya" else 0
total_tarif_pengiriman = tarif_dasar + biaya_express

print("total tarif pengiriman adalah : Rp{total_tarif_pengiriman}")