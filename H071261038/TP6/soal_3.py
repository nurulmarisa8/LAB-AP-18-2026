# Sistem Manajemen Playlist Musk (PlayTune)

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    genre_format = genre.strip().capitalize()
    playlist.append((judul, artis, genre_format, durasi))
    genre_set.add(genre_format)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist kosong.")
        return
    
    print("=" * 65)
    print(f"{'No':<4} {'Judul':<25} {'Artis':<15} {'Genre':<10} {'Durasi':<6}")
    print("=" * 65)
    
    total_detik = 0
    for i, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu
        total_detik += durasi
        menit = durasi // 60
        detik = durasi % 60
        format_durasi = f"{menit}:{detik:02d}"
        print(f"{i:<4} {judul:<25} {artis:<15} {genre:<10} {format_durasi:<6}")
        
    print("=" * 65)
    total_menit = total_detik // 60
    sisa_detik = total_detik % 60
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik")

def filter_genre(playlist, genre_target):
    target_format = genre_target.strip().capitalize()
    hasil = [lagu for lagu in playlist if lagu[2] == target_format]
    return hasil

def hapus_lagu(playlist, nomor):
    try:
        indeks = nomor - 1
        lagu_dihapus = playlist.pop(indeks)
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus dari playlist.")
    except IndexError:
        print("Nomor lagu tidak valid atau tidak ditemukan dalam playlist.")

def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist kosong, belum ada statistik.")
        return
        
    total_lagu = len(playlist)
    jumlah_genre = len(genre_set)
    
    distribusi = {genre: 0 for genre in genre_set}
    for lagu in playlist:
        genre_lagu = lagu[2]
        if genre_lagu in distribusi:
            distribusi[genre_lagu] += 1
            
    lagu_terpanjang = max(playlist, key=lambda x: x[3])
    lagu_terpendek = min(playlist, key=lambda x: x[3])
    
    def format_waktu(detik):
        m = detik // 60
        d = detik % 60
        return f"{m}:{d:02d}"

    print("=" * 45)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 45)
    print(f"Total lagu     : {total_lagu}")
    print(f"Jumlah genre   : {jumlah_genre}")
    print(f"Daftar genre   : {genre_set}")
    print("\nDistribusi genre:")
    for g, count in distribusi.items():
        print(f"  {g:<12} : {'#' * count} ({count})")
    print(f"\nLagu terpanjang : {lagu_terpanjang[0]} ({format_waktu(lagu_terpanjang[3])})")
    print(f"Lagu terpendek  : {lagu_terpendek[0]} ({format_waktu(lagu_terpendek[3])})")
    print("=" * 45)

# Main Program PlayTune
def main_playtune():
    playlist = []
    genre_set = set()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter Berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == "1":
            judul = input("Judul lagu: ")
            artis = input("Artis: ")
            genre = input("Genre: (Pop/Rock/Jazz/Rnb/Dangdut)")
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Durasi harus angka positif!")
                    continue
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Durasi harus berupa angka bulat (detik)!")
        elif pilihan == "2":
            tampilkan_playlist(playlist)
        elif pilihan == "3":
            print(f"Genre tersedia: {genre_set}")
            target = input("Masukkan genre yang ingin difilter: ")
            hasil_filter = filter_genre(playlist, target)
            print(f"\nLagu bergenre '{target}':")
            for i, l in enumerate(hasil_filter, 1):
                menit, detik = l[3] // 60, l[3] % 60
                print(f"  {i}. {l[0]} - {l[1]} ({menit}:{detik:02d})")
        elif pilihan == "4":
            tampilkan_playlist(playlist)
            if playlist:
                try:
                    no = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                    hapus_lagu(playlist, no)
                except ValueError:
                    print("Nomor harus berupa angka!")
        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)
        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan menu tidak valid.")

main_playtune()
