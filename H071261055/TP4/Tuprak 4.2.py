def rekap_nilai(*args):
    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)

    return rata_rata, nilai_tertinggi, nilai_terendah

nilai_siswa = []

while True:
    input_nilai = input("Masukkan nilai siswa (kosongkan untuk selesai): ")
    if input_nilai == "":
        break
    nilai_siswa.append(float(input_nilai))

if len(nilai_siswa) == 0:
    print("data nilai tidak tersedia.")
else:
    rata_rata, nilai_tertinggi, nilai_terendah = rekap_nilai(*nilai_siswa)
    
    print(f"Rata-rata nilai: {rata_rata}")
    print(f"Nilai tertinggi: {nilai_tertinggi:.0f}")
    print(f"Nilai terendah: {nilai_terendah:.0f}")