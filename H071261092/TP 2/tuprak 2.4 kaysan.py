tujuan = input("masukkan tujuan (pantai/pegunungan/kota) :")
waktu = input("masukkan waktu (malam/pagi) : ")
tipe_pengunjung = input("masukkan tipe pengunjung (anak/dewasa) : ")

match tujuan:
    case "pantai":
        if waktu == "pagi":
             print("Paket Rekomendasi : Paket A")
        elif waktu == "malam" and tipe_pengunjung == "dewasa":
            print("Paket Rekomendasi : Paket C")
        else:
            print("tidak ada paket yang cocok")
            
    case "pegunungan":
        if waktu == "pagi" and tipe_pengunjung == "dewasa":
            print("Paket Rekomendasi : Paket B")
        elif waktu == "malam" and tipe_pengunjung == "dewasa":
            print("Paket Rekomendasi : Paket C")
        else:
            print("tidak ada paket yang cocok")
            
    case "kota":
        if waktu == "malam":
            print("Paket Rekomendasi : Paket C")
        else:
            print("tidak ada paket yang cocok")

    case _:
        print("tidak ada paket yang cocok")