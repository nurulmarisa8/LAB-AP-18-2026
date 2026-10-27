kandidat = set()
rekap_suara_nya = {}

def daftar_kandidat(kandidat_set, nama):
    if nama in kandidat_set:
        print(f"'{nama}' telah ada di dalam daftar!")
        return False
    kandidat_set.add(nama)
    print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    return True

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih = nama_pemilih.lower()
    if pemilih in rekap_suara:
        print(f"'{nama_pemilih.title()}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Tidak ada kandidat dengan nama '{pilihan}'")
    else:
        rekap_suara[pemilih] = pilihan
        print(f"Suara '{nama_pemilih.title()}' untuk '{pilihan}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in sorted(kandidat_set):
        perolehan[kandidat] = 0
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    tertinggi = max(perolehan.values())
    pemenang = [nama for nama, suara in perolehan.items() if suara == tertinggi]
    ada_berapa_pemilih = sum(perolehan.values())
    print()
    print("=================================")
    print("   HASIL PEMILIHAN KETUA KELAS")
    print("=================================")
    for key, value in perolehan.items():
        print(f"   {key}: {value} suara")
    print()
    print(f"Total suara masuk: {ada_berapa_pemilih}")
    if ada_berapa_pemilih == 0:
        print("Belum ada suara masuk, pemenang belum dapat ditentukan")
    elif len(pemenang) > 1:
        print("Hasil SERI antara: " + ", ".join(pemenang))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")

print("==================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("==================================")
print("--- FASE PENDAFTARAN KANDIDAT ---")
while True:
    nama_kandidat = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip().capitalize()
    if nama_kandidat == "":
        if len(kandidat) < 2:
            print("Minimal ada 2 kandidat untuk melanjutkan")
            continue
        print()
        break
    daftar_kandidat(kandidat, nama_kandidat)

print(f"Kandidat terdaftar: {kandidat}")
print()
print("--- FASE PEMUNGUTAN SUARA ---")
while True:
    print()
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {kandidat}")
    pilih_kandidat = input("Pilih kandidat: ").strip().capitalize()
    if pilih_kandidat == "":
        print("Nama kandidat tidak boleh kosong")
        continue
    berikan_suara(rekap_suara_nya, kandidat, nama_pemilih, pilih_kandidat)
perolehan = hitung_suara(rekap_suara_nya, kandidat)
tampilkan_hasil(perolehan)
