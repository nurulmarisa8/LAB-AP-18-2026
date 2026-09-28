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
        elif waktu == "Malam" and pengunjung == "Dewasa":
            rekomendasi = "Paket C"
        else:
            rekomendasi = "Tidak ada paket yang cocok"

    case _:
        rekomendasi = "Tidak ada paket yang cocok"

print (f"Paket Rekomendasi: {rekomendasi}")