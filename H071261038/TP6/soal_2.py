# Sistem Pemilihan Ketua Kelas (Vote Class)

def daftar_kandidat(kandidat_set, nama):
    kandidat_format = nama.strip().capitalize()
    if kandidat_format in kandidat_set:
        print(f"'{kandidat_format}' sudah terdaftar!")
    else:
        kandidat_set.add(kandidat_format)
        print(f"'{kandidat_format}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_key = nama_pemilih.strip().lower()
    pilihan_format = pilihan.strip().capitalize()
    
    if pemilih_key in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return
    
    if pilihan_format not in kandidat_set:
        print("Pesan error: Kandidat tidak tersedia atau tidak ada di dalam set!")
        return
    
    rekap_suara[pemilih_key] = pilihan_format
    print(f"Suara '{nama_pemilih}' untuk '{pilihan_format}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    for pilihan in rekap_suara.values():
        if pilihan in perolehan:
            perolehan[pilihan] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    print("\n" + "=" * 40)
    print("HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)
    for kandidat, suara in perolehan.items():
        print(f"{kandidat}: {suara} suara")
    
    total_suara = sum(perolehan.values())
    print(f"\nTotal suara masuk: {total_suara}")
    
    if total_suara == 0:
        print("Tidak ada suara yang masuk.")
        return

    max_suara = max(perolehan.values())
    pemenang = [k for k, v in perolehan.items() if v == max_suara]
    
    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {max_suara} suara!")
    print("=" * 40)

# Main Program VoteClass
def main_voteclass():
    kandidat_set = set()
    rekap_suara = {}
    
    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
        if nama == "":
            if len(kandidat_set) < 2:
                print("Minimal harus ada 2 kandidat sebelum bisa lanjut!")
                continue
            break
        daftar_kandidat(kandidat_set, nama)
        
    print(f"\nKandidat terdaftar: {kandidat_set}")
    
    print("\n--- FASE PEMUNGUTAN SUARA ---")
    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
        if nama_pemilih == "":
            break
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
        
    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

main_voteclass()
