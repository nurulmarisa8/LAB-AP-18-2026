# Soal 3
nilai = int(input("masukkan nilai tes: "))
if nilai >= 80:
    status =("lolos ke tahap wawancara")

elif nilai >= 65 and pengalaman >= 2:
    pengalaman = int(input("masukkan pengalaman kerja: "))
    status =("lolos bersyarat")
else:
    status =("tidak lolos")

print(status)
