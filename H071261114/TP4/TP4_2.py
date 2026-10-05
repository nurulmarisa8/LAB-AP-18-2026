def rekap_nilai(*args):
    if not args:
        return None
    rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)
    return rata, tertinggi, terendah

# Menampung input nilai secara dinamis
daftar_nilai = []
while True:
    user_input = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if user_input == "":
        break
    daftar_nilai.append(float(user_input))

# Memanggil function dengan unpacking list (*)
hasil = rekap_nilai(*daftar_nilai)

if hasil is None:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = hasil
    # Menampilkan format float jika ada koma, atau int jika bilangan bulat
    print(f"Rata-rata kelas: {rata if rata % 1 != 0 else int(rata)}")
    print(f"Nilai tertinggi: {int(tertinggi) if tertinggi % 1 == 0 else tertinggi}")
    print(f"Nilai terendah: {int(terendah) if terendah % 1 == 0 else terendah}")