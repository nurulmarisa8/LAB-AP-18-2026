def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    for lagu in playlist:
        if lagu[0].lower() == judul.lower() and lagu[1].lower() == artis.lower():
            print(f"Gagal: Lagu '{judul}' oleh {artis} sudah ada di dalam playlist!")
            return False 
    if durasi <= 0:
        print("Gagal: Durasi harus berupa angka positif!")
        return False
        
    lagu_baru = (judul, artis, genre, durasi)
    playlist.append(lagu_baru)
    genre_set.add(genre)
    
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")
    return True

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return
        
    print("=======================================================")
    print("No  Judul               Artis          Genre    Durasi")
    print("=======================================================")
    
    total_detik_playlist = 0
    nomor = 1
    
    for lagu in playlist:
        judul, artis, genre, durasi_detik = lagu
        menit = durasi_detik // 60
        detik = durasi_detik % 60
        
        teks_detik = str(detik)
        if detik < 10:
            teks_detik = "0" + teks_detik
            
        print(f"{nomor}   {judul:<20}{artis:<13}  {genre:<7}  {menit}:{teks_detik}")
        
        total_detik_playlist += durasi_detik
        nomor += 1
        
    print("=======================================================")
    total_menit = total_detik_playlist // 60
    total_sisa_detik = total_detik_playlist % 60
    print(f"Total durasi playlist: {total_menit} menit {total_sisa_detik} detik")

def filter_genre(playlist, genre_target):
    hasil_filter = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    return hasil_filter

def hapus_lagu(playlist, nomor):
    indeks = nomor - 1
    if indeks < 0 or indeks >= len(playlist):
        print("Error: Nomor lagu tidak valid.")
        return False
        
    lagu_dihapus = playlist.pop(indeks)
    print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus dari playlist!")
    return True

def statistik_playlist(playlist, genre_set):
    print("========================================")
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    
    total_lagu = len(playlist)
    jumlah_genre_unik = len(genre_set)
    
    print(f" Total lagu     : {total_lagu}")
    print(f" Jumlah genre   : {jumlah_genre_unik}")
    print(f" Daftar genre   : {genre_set}")
    
    if not playlist:
        print("========================================")
        return
        
    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        if genre in distribusi:
            distribusi[genre] += 1
        else:
            distribusi[genre] = 1
            
    print(" Distribusi genre:")
    for gen, jumlah in distribusi.items():
        simbol_pagar = "# " * jumlah
        print(f"  {gen:<10} : {simbol_pagar}({jumlah})")
        
    lagu_terpanjang = playlist[0]
    lagu_terpendek = playlist[0]
    
    for lagu in playlist:
        if lagu[3] > lagu_terpanjang[3]:
            lagu_terpanjang = lagu
        if lagu[3] < lagu_terpendek[3]:
            lagu_terpendek = lagu
            
    menit_panjang = lagu_terpanjang[3] // 60
    detik_panjang = lagu_terpanjang[3] % 60
    teks_detik_panjang = str(detik_panjang)
    if detik_panjang < 10: teks_detik_panjang = "0" + teks_detik_panjang
    
    menit_pendek = lagu_terpendek[3] // 60
    detik_pendek = lagu_terpendek[3] % 60
    teks_detik_pendek = str(detik_pendek)
    if detik_pendek < 10: teks_detik_pendek = "0" + teks_detik_pendek
            
    print(f" Lagu terpanjang : {lagu_terpanjang[0]} ({menit_panjang}:{teks_detik_panjang})")
    print(f" Lagu terpendek  : {lagu_terpendek[0]} ({menit_pendek}:{teks_detik_pendek})")
    print("========================================")

playlist_musik = []
genre_tersedia = set()

print("========================================")
print("  PLAYLIST MUSIK - PLAYTUNE")
print("========================================")

while True:
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
        try:
            durasi = int(input("Durasi (dalam detik): "))
            tambah_lagu(playlist_musik, genre_tersedia, judul, artis, genre, durasi)
        except ValueError:
            print("Gagal: Durasi harus berupa angka!")
            
    elif pilihan == "2":
        tampilkan_playlist(playlist_musik)
        
    elif pilihan == "3":
        print(f"Genre tersedia: {genre_tersedia}")
        target = input("Masukkan genre yang ingin difilter: ")
        hasil = filter_genre(playlist_musik, target)
        
        if hasil:
            print(f"Lagu bergenre '{target}':")
            no = 1
            for lagu in hasil:
                menit = lagu[3] // 60
                detik = lagu[3] % 60
                teksdetik = str(detik) if detik >= 10 else "0" + str(detik)
                print(f" {no}. {lagu[0]} - {lagu[1]} ({menit}:{teksdetik})")
                no += 1
        else:
            print(f"Tidak ada lagu dengan genre '{target}'.")
            
    elif pilihan == "4":
        tampilkan_playlist(playlist_musik)
        if playlist_musik:
            try:
                nomor_hapus = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist_musik, nomor_hapus)
            except ValueError:
                print("Gagal: Input harus berupa angka nomor urut!")
                
    elif pilihan == "5":
        statistik_playlist(playlist_musik, genre_tersedia)
        
    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-6.")
