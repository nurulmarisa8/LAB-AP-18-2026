# Rekap  Nilai Ujian (Arbitrary Arguments)

def rekap_nilai(*args):
    if not args:
        return None, None, None

    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)

    return rata_rata, tertinggi, terendah

def main_rekap():
    daftar_nilai = []

    while True:
        inp = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
        if inp == "":
            break
        daftar_nilai.append(float(inp))

    if not daftar_nilai:
        print("Data nilai tidak tersedia")

    else:
        rata_rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)

        # Rata-rata jika bulat ditampilkan .0
        if rata_rata.is_integer():
            fmt_rata =f"{rata_rata:.1f}"
        else:
            fmt_rata =f"{rata_rata}"

        print(f"Rata-rata kelas: {fmt_rata}")
        print(f"Nilai tertinggi: {int(tertinggi) if tertinggi.is_integer() else tertinggi}")
        print(f"Nilai terendah: {int(terendah) if terendah.is_integer() else terendah}")

if __name__ == "__main__":
    main_rekap()