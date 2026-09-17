tujuan = (input("Masukkan tujuan (Pantai/Pegunungan/Kota): "))
waktu =  (input("Masukkan waktu (Pagi/Malam): "))
tipe_orang =  (input("Masukkan tipe pengunjung (Anak/Dewasa): "))
paket = ("Tidak ada paket yang cocok")
match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            paket = "Paket A"
    case "Pegunungan":
        if waktu == "Pagi" and tipe_orang == "Dewasa" :
            paket = "Paket B"
    case "Kota":
        if waktu == "Malam":
            paket = "Paket C"
    case _ :
        print(paket)

if waktu == "Malam" and tipe_orang == "Dewasa":
            paket = "Paket C"
print ("Paket Rekomendasi:", paket)