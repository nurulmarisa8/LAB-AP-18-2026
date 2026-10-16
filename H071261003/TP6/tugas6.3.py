def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)

    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    print("\n=======================================================")
    print(f"{'No':<4}{'Judul':<21}{'Artis':<15}{'Genre':<10}Durasi")
    print("=======================================================")

    total_durasi = 0

    for nomor, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu
        menit = durasi // 60
        detik = durasi % 60

        print(
            f"{nomor:<4}{judul:<21}{artis:<15}"
            f"{genre:<10}{menit}:{detik:02d}"
        )

        total_durasi += durasi

    print("=======================================================")
    print(
        f" Total durasi playlist: "
        f"{total_durasi // 60} menit "
        f"{total_durasi % 60} detik"
    )


def filter_genre(playlist, genre_target):
    hasil_filter = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil_filter


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Error: Nomor lagu tidak valid!")
        return

    lagu = playlist.pop(nomor - 1)
    print(f"Lagu '{lagu[0]}' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    distribusi_genre = {}

    for lagu in playlist:
        genre = lagu[2]

        if genre not in distribusi_genre:
            distribusi_genre[genre] = 0

        distribusi_genre[genre] += 1

    lagu_terpanjang = max(playlist, key=lambda lagu: lagu[3])
    lagu_terpendek = min(playlist, key=lambda lagu: lagu[3])

    print("\n========================================")
    print("       STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    print(f"Total lagu        : {len(playlist)}")
    print(f"Jumlah genre      : {len(genre_set)}")
    print(f"Daftar genre      : {genre_set}")
    print("\nDistribusi genre:")

    for genre in sorted(distribusi_genre):
        print(f"  {genre:<10}: # ({distribusi_genre[genre]})")

    print(
        f"\nLagu terpanjang   : {lagu_terpanjang[0]} "
        f"({lagu_terpanjang[3] // 60}:"
        f"{lagu_terpanjang[3] % 60:02d})"
    )

    print(
        f"Lagu terpendek    : {lagu_terpendek[0]} "
        f"({lagu_terpendek[3] // 60}:"
        f"{lagu_terpendek[3] % 60:02d})"
    )

    print("========================================")


playlist = []
genre_set = set()

print("========================================")
print("   PLAYLIST MUSIK - PLAYTUNE")
print("========================================")

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        judul = input("Judul lagu: ").strip()
        artis = input("Artis: ").strip()
        genre = input(
            "Genre (Pop/Rock/Jazz/RnB/Dangdut): "
        ).strip().capitalize()

        try:
            durasi = int(input("Durasi (dalam detik): "))

            if durasi <= 0:
                print("Error: Durasi harus berupa angka positif!")

            elif judul == "" or artis == "" or genre == "":
                print(
                    "Error: Judul, artis, dan genre "
                    "tidak boleh kosong!"
                )

            else:
                tambah_lagu(
                    playlist,
                    genre_set,
                    judul,
                    artis,
                    genre,
                    durasi
                )

        except ValueError:
            print("Error: Durasi harus berupa angka!")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Playlist masih kosong.")

        else:
            print("Genre tersedia:", genre_set)

            genre_target = input(
                "Masukkan genre yang ingin difilter: "
            ).strip()

            hasil_filter = filter_genre(playlist, genre_target)

            if len(hasil_filter) == 0:
                print(f"Tidak ada lagu bergenre '{genre_target}'.")

            else:
                print(f"\nLagu bergenre '{genre_target}':")

                for nomor, lagu in enumerate(hasil_filter, start=1):
                    judul, artis, genre, durasi = lagu
                    menit = durasi // 60
                    detik = durasi % 60

                    print(
                        f"  {nomor}. {judul} - {artis} "
                        f"({menit}:{detik:02d})"
                    )

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong.")

        else:
            tampilkan_playlist(playlist)

            try:
                nomor = int(
                    input("Masukkan nomor lagu yang ingin dihapus: ")
                )

                jumlah_genre_sebelum = len(genre_set)
                hapus_lagu(playlist, nomor)

                genre_set.clear()

                for lagu in playlist:
                    genre_set.add(lagu[2])

            except ValueError:
                print("Error: Nomor lagu harus berupa angka!")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Error: Pilihan menu harus antara 1-6!")