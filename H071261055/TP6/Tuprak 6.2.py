def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip()
    if not nama.replace(" ", "").isalpha():
        raise ValueError("Nama kandidat hanya boleh berisi huruf!")
    nama = nama.capitalize()
    if nama in kandidat_set:
        raise ValueError(f"'{nama}' sudah terdaftar sebagai kandidat!")
    kandidat_set.add(nama)
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    kunci_pemilih = nama_pemilih.strip().lower()
    pilihan = pilihan.strip().capitalize()

    if kunci_pemilih in rekap_suara:
        raise ValueError(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
    if pilihan not in kandidat_set:
        raise ValueError(f"Kandidat '{pilihan}' tidak ada dalam daftar! "
                         f"Suara tidak dicatat.")

    rekap_suara[kunci_pemilih] = pilihan
    print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    for pilihan in rekap_suara.values():
        if pilihan not in perolehan:
            raise ValueError(f"Suara untuk '{pilihan}' tidak valid!")
        perolehan[pilihan] += 1
    return perolehan


def tampilkan_hasil(perolehan):
    if not perolehan:
        raise ValueError("Tidak ada kandidat untuk ditampilkan!")
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)
    for kandidat in sorted(perolehan):
        print(f" {kandidat}: {perolehan[kandidat]} suara")

    total = sum(perolehan.values())
    print(f"Total suara masuk: {total}")

    suara_tertinggi = max(perolehan.values())
    pemenang = sorted(k for k, v in perolehan.items() if v == suara_tertinggi)

    if total == 0:
        print("Belum ada suara yang masuk.")
    elif len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
    print("=" * 40)


def main():
    kandidat_set = set()
    rekap_suara = {}

    print("=" * 40)
    print(" SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)

    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(kandidat_set) < 2:
                print("Error: minimal harus ada 2 kandidat sebelum lanjut!")
                continue
            break
        try:
            daftar_kandidat(kandidat_set, nama)
        except ValueError as e:
            print(f"Error: {e}")
    print(f"Kandidat terdaftar: {kandidat_set}")

    print("--- FASE PEMUNGUTAN SUARA ---")
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
        if nama_pemilih == "":
            break
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        try:
            berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
        except ValueError as e:
            print(f"Error: {e}")

    try:
        perolehan = hitung_suara(rekap_suara, kandidat_set)
        tampilkan_hasil(perolehan)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()