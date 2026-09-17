# Tarif Pengiriman Barang

jarak = int(input("masukkan jarak pengiriman barang (km) :"))
layanan_express = input("layanan expres (ya/tidak) :")

if jarak < 5:
    tarif = 10000
elif jarak <=20:
    tarif = 20000
else:
    tarif = 35000

layanan = 15000 if layanan_express == "ya" else 0
total = tarif + layanan
print("tarif pengiriman: Rp", total)