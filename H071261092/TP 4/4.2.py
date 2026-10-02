def rekap_nilai(*args):
    rata_rata = sum(args) / len(args) 
    tertinggi = max(args)
    terendah = min(args)
    return rata_rata, tertinggi, terendah

daftar_nilai = []
while True:
        nilai = input("Masukkan nilai ujian (atau kosongkan untuk mengakhiri): ")
        if nilai == "":
            break
        try:
            nilai = float(nilai)
            daftar_nilai.append(nilai)
            hasil = rekap_nilai(*daftar_nilai)
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka atau 'selesai'.")

rata_rata, tertinggi, terendah = hasil
print(f"Rata-rata nilai ujian: {rata_rata}")
print(f"Nilai tertinggi: {tertinggi}")
print(f"Nilai terendah: {terendah}")