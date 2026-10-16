def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
        return

    kandidat_set.add(nama)
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_kunci = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if nama_kunci in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return

    if pilihan not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak ditemukan!")
        return

    rekap_suara[nama_kunci] = pilihan
    print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("\n========================================")
    print("  HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    for kandidat in sorted(perolehan):
        print(f"  {kandidat}: {perolehan[kandidat]} suara")

    total_suara = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total_suara}")

    suara_tertinggi = max(perolehan.values())
    pemenang = []

    for kandidat, suara in perolehan.items():
        if suara == suara_tertinggi:
            pemenang.append(kandidat)

    if len(pemenang) > 1:
        print("Hasil SERI antara:", ", ".join(sorted(pemenang)))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(
            f"PEMENANG: {pemenang[0]} "
            f"dengan {suara_tertinggi} suara!"
        )

    print("========================================")


kandidat_set = set()
rekap_suara = {}

print("========================================")
print("  SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    try:
        nama = input(
            "Masukkan nama kandidat (kosongkan untuk selesai): "
        )

        if nama.strip() == "":
            break

        daftar_kandidat(kandidat_set, nama.strip())

    except (EOFError, KeyboardInterrupt):
        print("\nPendaftaran kandidat dihentikan.")
        break

if len(kandidat_set) < 2:
    print("Error: Minimal harus ada 2 kandidat.")

else:
    print("\nKandidat terdaftar:", kandidat_set)
    print("\n--- FASE PEMUNGUTAN SUARA ---")

    while True:
        try:
            nama_pemilih = input(
                "\nNama pemilih (kosongkan untuk selesai): "
            )

            if nama_pemilih.strip() == "":
                break

            print("Kandidat yang tersedia:", kandidat_set)
            pilihan = input("Pilih kandidat: ")

            berikan_suara(
                rekap_suara,
                kandidat_set,
                nama_pemilih.strip(),
                pilihan.strip()
            )

        except (EOFError, KeyboardInterrupt):
            print("\nPemungutan suara dihentikan.")
            break

    try:
        perolehan = hitung_suara(rekap_suara, kandidat_set)
        tampilkan_hasil(perolehan)

    except (TypeError, KeyError, ValueError) as error:
        print(f"Terjadi kesalahan saat menghitung hasil: {error}")