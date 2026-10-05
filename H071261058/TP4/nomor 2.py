def jumlah(*args):
    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)
    return rata_rata, tertinggi, terendah


daftar_nilai = []
while True:
    teks = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if teks == "":
        break
    nilai = int(teks)
    daftar_nilai.append(nilai)

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = jumlah(*daftar_nilai)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")