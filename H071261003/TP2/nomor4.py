tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input ("Masukkan waktu (Pagi/Malam):")
tipe = input ("Masukkan tipe pengunjung(Anak/Dewasa):")

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket Rekomendasi: Paket A")
        else:
            if tipe == "Dewasa":
                print("Paket Rekomendasi: Paket C")
            else:
                print("Tidak ada paket yang cocok")

    case "Pegunungan":
        if waktu == "Pagi":
            if tipe == "Dewasa":
                print("Paket Rekomendasi: Paket B")
            else:
                print("Tidak ada paket yang cocok")
        else:
            if tipe == "Dewasa":
                print("Tidak ada paket yang cocok")
    

    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        else: 
            print("Tidak ada paket yang cocok")

    case _:
        print("Tidak ada paket yang cocok")