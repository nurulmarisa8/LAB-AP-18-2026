# Soal 4
tujuan = input("masukkan tujuan (pantai/pegunungan/kota): ")
waktu = input("masukkan waktu (pagi/malam): ")
tipe = input("masukkan tipe pengunjung(anak/dewasa): ")

paket = "tidak ada paket yang cocok"

# Menggunakan match case
match tujuan:
    case"pantai":
        if waktu == "pagi":
            paket = "paket A"
        elif waktu == "malam" and tipe == "dewasa":
            paket = "paket C"

    case"pegunungan":
        if waktu == "pagi" and tipe == "dewasa":
            paket = "paket B"
        elif waktu == "malam" and tipe == "dewasa":
            paket = "paket C"

    case"kota":
        if waktu == "malam":
            paket = "paket C"

print(f"paket rekomendasi: {paket}")