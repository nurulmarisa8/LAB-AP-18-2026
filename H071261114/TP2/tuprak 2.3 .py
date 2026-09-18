tes = int(input("Masukkan nilai tes : "))

if tes >= 80:
    print("Lolos ke Tahap Wawancara")
elif tes < 80 and tes >= 65:
    pengalaman = int(input("Masukkan pengalaman kerja (tahun) : "))
    if pengalaman >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")
else:
    print("Tidak Lolos")