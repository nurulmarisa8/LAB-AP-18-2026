def rekap_nilai(*args):
    rata_rata = round(sum(args) / len(args), 2)
    nilai_tertinggi = round(max(args))
    nilai_terendah = round(min(args))

    return rata_rata, nilai_tertinggi, nilai_terendah

nilai_siswa = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai):")

    if input_nilai== "":
        break

    nilai = float(input_nilai)
    nilai_siswa.append(nilai)

if len(nilai_siswa) == 0:
    print("Data nilai tidak tersedia.")

else:
    rata_rata,nilai_tertinggi, nilai_terendah = rekap_nilai(*nilai_siswa)

    print(f"Rata_rata kelas: {rata_rata}")
    print(f"Nilai_tertinggi: {nilai_tertinggi}")
    print(f"Nilai_terendah: {nilai_terendah}")