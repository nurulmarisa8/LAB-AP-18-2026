# Tingkat Kepedasan

persentase = int(input("masukkan tingkat kepedasan cabai : "))

if persentase < 0:
     print("input tidak valid")
elif persentase >= 0 and persentase <= 10:
     print("level aman")
elif persentase >= 11 and persentase <= 40:
     print("level sedang")
elif persentase >= 41 and persentase <= 70:
     print("level pedas")
else:
     print("level ekstrem")





# Tiket Perjalanan

# tujuan = input("masukkan tujuan (pantai/pegunungan/kota): ")
# waktu = input("masukkan waktu (pagi/malam): ")
# tipe_pengunjung = input("masukkan tipe pengunjung (anak/dewasa): ")

# paket = "tidak ada paket yang cocok"

# match tujuan:
#     case "pantai":
#         if waktu == "pagi":
#           print("paket rekomendasi: paket a")
#         elif waktu  == "malam" and tipe_pengunjung == "dewasa":
#           print("paket rekomendasi: paket c")

#     case "pegunungan":
#         if waktu == "pagi" and tipe_pengunjung == "dewasa":
#           print("paket rekomendasi: paket b")
#         elif waktu == "malam" and tipe_pengunjung == "dewasa":
#           print("paket rekomendasi: paket c")

#     case "kota":
#         if waktu == "malam":
#           print("paket rekmendasi: paket c")