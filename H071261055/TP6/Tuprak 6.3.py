def baca_angka(prompt, nama):
    """Membaca input angka bulat. Jika bukan angka -> ValueError."""
    try:
        return int(input(prompt))
    except ValueError:
        raise ValueError(f"{nama} harus berupa angka!") from None


def format_durasi(detik):
    return f"{detik // 60}:{detik % 60:02d}"


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    if judul.strip() == "" or artis.strip() == "" or genre.strip() == "":
        raise ValueError("Judul, artis, dan genre tidak boleh kosong!")
    if durasi <= 0:
        raise ValueError("Durasi harus berupa angka positif!")
    for g in genre_set:
        if g.lower() == genre.lower():
            genre = g
            break
    lagu = (judul, artis, genre, durasi) 
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if not playlist:
        raise ValueError("Playlist masih kosong!")
    print("=" * 55)
    print(f"{'No':<4}{'Judul':<24}{'Artis':<16}{'Genre':<8}{'Durasi'}")
    print("=" * 55)
    total = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, 1):
        print(f"{i:<4}{judul:<24}{artis:<16}{genre:<8}{format_durasi(durasi)}")
        total += durasi
    print("=" * 55)
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik")


def filter_genre(playlist, genre_target):
    if genre_target.strip() == "":
        raise ValueError("Genre tidak boleh kosong!")
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if not playlist:
        raise ValueError("Playlist masih kosong!")
    if not 1 <= nomor <= len(playlist):
        raise ValueError(f"Nomor lagu tidak valid! Pilih 1 sampai {len(playlist)}.")
    lagu = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu[0]}' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    if not playlist:
        raise ValueError("Playlist masih kosong!")

    distribusi = {}
    for lagu in playlist:
        distribusi[lagu[2]] = distribusi.get(lagu[2], 0) + 1

    terpanjang = max(playlist, key=lambda lagu: lagu[3])
    terpendek = min(playlist, key=lambda lagu: lagu[3])

    print("=" * 40)
    print(" STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    print(f" Total lagu : {len(playlist)}")
    print(f" Jumlah genre : {len(genre_set)}")
    print(f" Daftar genre : {genre_set}")
    print(" Distribusi genre:")
    for genre, jumlah in distribusi.items():
        print(f" {genre} : {'#' * jumlah} ({jumlah})")
    print(f" Lagu terpanjang : {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f" Lagu terpendek : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 40)


def main():
    playlist = []
    genre_set = set()

    print("=" * 40)
    print(" PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)

    while True:
        print("Menu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        try:
            pilihan = baca_angka("Pilih menu (1-6): ", "Pilihan menu")

            if pilihan == 1:
                judul = input("Judul lagu: ")
                artis = input("Artis: ")
                genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()
                durasi = baca_angka("Durasi (dalam detik): ", "Durasi")
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            elif pilihan == 2:
                tampilkan_playlist(playlist)
            elif pilihan == 3:
                print(f"Genre tersedia: {genre_set}")
                target = input("Masukkan genre yang ingin difilter: ").strip()
                hasil = filter_genre(playlist, target)
                if not hasil:
                    raise ValueError(f"Tidak ada lagu bergenre '{target}'.")
                print(f"Lagu bergenre '{target}':")
                for i, (judul, artis, _, durasi) in enumerate(hasil, 1):
                    print(f" {i}. {judul} - {artis} ({format_durasi(durasi)})")
            elif pilihan == 4:
                tampilkan_playlist(playlist)
                nomor = baca_angka("Nomor lagu yang ingin dihapus: ", "Nomor lagu")
                hapus_lagu(playlist, nomor)
            elif pilihan == 5:
                statistik_playlist(playlist, genre_set)
            elif pilihan == 6:
                print("Terima kasih telah menggunakan PlayTune!")
                break
            else:
                raise ValueError("Pilihan menu harus antara 1 sampai 6!")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()