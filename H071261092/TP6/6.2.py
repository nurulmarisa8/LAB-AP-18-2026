def daftar_kandidat(kandidat_set, nama):
    nama_kapital = nama.capitalize()
    
    if nama_kapital in kandidat_set:
        print(f"Gagal: Kandidat '{nama_kapital}' sudah terdaftar!")
        return False
    else:
        kandidat_set.add(nama_kapital)
        print(f"'{nama_kapital}' berhasil didaftarkan sebagai kandidat!")
        return True

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_lower = nama_pemilih.lower()
    pilihan_kapital = pilihan.capitalize()
    
    if pemilih_lower in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return False
        
    if pilihan_kapital not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak ada dalam set kandidat!")
        return False
        
    rekap_suara[pemilih_lower] = pilihan_kapital
    print(f"Suara '{nama_pemilih}' untuk '{pilihan_kapital}' berhasil dicatat!")
    return True

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
        
    for kandidat_terpilih in rekap_suara.values():
        if kandidat_terpilih in perolehan:
            perolehan[kandidat_terpilih] += 1
            
    return perolehan

def tampilkan_hasil(perolehan):
    print("========================================")
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("========================================")
    
    total_suara = sum(perolehan.values())
    
    for kandidat, suara in perolehan.items():
        print(f" {kandidat}: {suara} suara")
        
    print(f"Total suara masuk: {total_suara}")
    
    if total_suara == 0:
        print("Belum ada suara yang masuk.")
        print("========================================")
        return

    suara_tertinggi = -1
    for suara in perolehan.values():
        if suara > suara_tertinggi:
            suara_tertinggi = suara
            
    daftar_pemenang = []
    for kandidat, suara in perolehan.items():
        if suara == suara_tertinggi:
            daftar_pemenang.append(kandidat)
            
    if len(daftar_pemenang) > 1:
        nama_seri = ", ".join(daftar_pemenang)
        print(f"Hasil SERI antara: {nama_seri}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        pemenang_tunggal = daftar_pemenang[0]
        print(f"PEMENANG: {pemenang_tunggal} dengan {suara_tertinggi} suara!")
        
    print("========================================")



kandidat_set = set()
rekap_suara = {}

print("========================================")
print(" SISTEM PEMILIHAN KETUA KELAS")
print("========================================")
print("--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
    if nama == "":
        if len(kandidat_set) < 2:
            print("Gagal: Minimal harus ada 2 kandidat sebelum bisa lanjut!")
            continue
        break
    daftar_kandidat(kandidat_set, nama)
    
print(f"Kandidat terdaftar: {kandidat_set}")

print("--- FASE PEMUNGUTAN SUARA ---")
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
    if nama_pemilih == "":
        break
        
    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ")
    
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
    
perolehan_akhir = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan_akhir)