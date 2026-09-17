# Tiket Perjalanan

tujuan = input("masukkan tujuan (pantai/pegunungan/kota): ")
waktu = input("masukkan waktu (pagi/malam): ")
tipe_pengunjung = input("masukkan tipe pengunjung (anak/dewasa): ")

paket = "tidak ada paket yang cocok"

match tujuan:
    case "pantai":
        if waktu == "pagi":
          print("paket rekomendasi: paket a")
        elif waktu  == "malam" and tipe_pengunjung == "dewasa":
          print("paket rekomendasi: paket c")
        else:
           print("Tidak Ada Paket Yang Cocok")

    case "pegunungan":
        if waktu == "pagi" and tipe_pengunjung == "dewasa":
          print("paket rekomendasi: paket b")
        elif waktu == "malam" and tipe_pengunjung == "dewasa":
          print("paket rekomendasi: paket c")
        else:
           print("Tidak Ada Paket Yang Cocok")

    case "kota":
        if waktu == "malam":
          print("paket rekmendasi: paket c")
        else:
           print("Tidak Ada Paket Yang Cocok")

