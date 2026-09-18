#Nomor 1
level_pedas = int(input("Masukkan persentase: "))

if level_pedas >= 0 and level_pedas <= 10:
    print ("Level Aman")
elif level_pedas >= 11 and level_pedas <= 40:
    print("Level Sedang")
elif level_pedas >= 41 and level_pedas <= 70:
    print("Level Pedas")
elif level_pedas >= 70 and level_pedas <= 100:
    print("Level Ekstrem")
else:
    print("Invalid")

#Nomor 2
jarak = int(input("Masukkan jarak pengiriman "))
express = input("Layanan express (ya/tidak): ")

if jarak < 5:
    jarak = 10000
elif jarak < 20:
    jarak = 20000
else:
    jarak = 35000

layanan = 15000 if express == "ya" else 0
tarif = jarak + layanan  
print ("total tarif pengiriman: Rp", tarif)

#Nomor 3
nilai = int(input("Masukkan nilai tes: "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun): ")) 

if nilai >= 80:
    print ("Lolos Ke Tahap Wawancara")
elif nilai >= 65 and pengalaman >= 2:
    print ("Lolos Bersyarat")
else:
    print ("Tidak Lolos")

#Nomor 4
tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").capitalize ()
waktu = input("Masukkan waktu (Pagi/Malam): ").capitalize ()
pengunjung = input("Masukkan tipe pengunjung (Anak/Dewasa): ").capitalize ()

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            rekomendasi = "Paket A"
        elif waktu == "Malam" and pengunjung == "Dewasa":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Tidak ada paket yang cocok"

    case "Pegunungan":
        if waktu == "Pagi" and pengunjung == "Dewasa":
            rekomendasi = "Paket B"
        elif waktu == "Malam" and pengunjung == "Dewasa":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Tidak ada paket yang cocok"

    case "Kota":
        if waktu == "Malam":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Tidak ada paket yang cocok"

    case _:
        rekomendasi = "Tidak ada paket yang cocok"

print (f"Paket Rekomendasi: {rekomendasi}")