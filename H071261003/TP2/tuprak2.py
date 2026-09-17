#SOAL NOMOR 1 KLASIFIKASI TINGKAT KEPEDASAN
persentase = int(input("Masukkan persentase cabai: "))

if persentase >= 0 and persentase <= 10:
    print("Level Aman")
elif persentase  >= 11 and persentase <= 40 :
    print("Level Sedang")
elif persentase  >= 41 and persentase <= 70 :
    print("Level Pedas")
elif persentase  > 70 and persentase <= 100:
    print("Level Ekstrem")
else:
    print("Input Tidak Valid")

#SOAL NOMOR 2 TARIF PENGIIRMANAN BARANG
jarak = int(input("Masukkan jarak pengiriman (dalam km): "))
express = input("Layanan Express (ya/tidak): ")

if jarak < 5:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
else:
    tarif = 35000

tambahan = 15000 if express == "ya" else 0
total = tarif + tambahan
print("Total tarif pengiriman: Rp", total)

#SOAL NOMOR 3 SELEKSI KARYAWAN
nilai = int(input("Masukkan nilai tes: "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

if nilai >= 80:
    print("Lolos ke Tahap Wawancara")
elif nilai >= 65 and pengalaman >= 2:
    print("Lolos Bersyarat")
else:
    print("Tidak lolos")

#SOAL NOMOR 4 REKOMENDASI PAKET WISATA
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


            


    