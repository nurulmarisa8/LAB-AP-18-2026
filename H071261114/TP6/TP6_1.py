def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    return buku


def cari_buku(inventaris, kata_kunci):
    kata_kunci = kata_kunci.lower()
    return [
        buku for buku in inventaris
        if kata_kunci in buku["judul"].lower()
    ]


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal: stok tidak boleh menjadi negatif.")
                return False

            buku["stok"] = stok_baru
            aksi = "bertambah" if jumlah >= 0 else "berkurang"
            print(
                f"Stok '{buku['judul']}' {aksi} {abs(jumlah)}. "
                f"Stok sekarang: {stok_baru}"
            )
            return True

    print(f"Error: buku '{judul}' tidak ditemukan.")
    return False


def ringkasan_inventaris(inventaris):
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah jenis buku : {len(inventaris)}")
    print(f"Total seluruh stok: {sum(buku['stok'] for buku in inventaris)}")

    total_aset = sum(
        buku["harga"] * buku["stok"] for buku in inventaris
    )
    print(f"Total nilai aset : Rp{total_aset:g}")

    if inventaris:
        buku_termahal = max(inventaris, key=lambda buku: buku["harga"])
        print(
            f"Buku termahal : {buku_termahal['judul']} "
            f"(Rp{buku_termahal['harga']:g})"
        )
    else:
        print("Buku termahal : Belum ada buku")

    print("=" * 40)


def input_angka(pesan, bilangan_bulat=False):
    while True:
        try:
            if bilangan_bulat:
                angka = int(input(pesan))
            else:
                angka = float(input(pesan))

            if angka < 0:
                print("Nilai tidak boleh negatif.")
                continue

            return angka
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def main():
    inventaris = []

    print("=" * 40)
    print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("=" * 40)

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            judul = input("Judul buku: ").strip()
            penulis = input("Penulis: ").strip()
            harga = input_angka("Harga: ")
            stok = input_angka("Stok awal: ", bilangan_bulat=True)

            tambah_buku(inventaris, judul, penulis, harga, stok)
            print(f"Buku '{judul}' berhasil ditambahkan!")

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ").strip()
            hasil = cari_buku(inventaris, kata_kunci)

            if hasil:
                print(f"Ditemukan {len(hasil)} buku:")
                for nomor, buku in enumerate(hasil, start=1):
                    print(
                        f"{nomor}. {buku['judul']} - {buku['penulis']} "
                        f"| Rp{buku['harga']:g} | Stok: {buku['stok']}"
                    )
            else:
                print("Tidak ada buku yang cocok.")

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ").strip()

            try:
                jumlah = int(
                    input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
                )
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Jumlah perubahan harus berupa bilangan bulat.")

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")


if __name__ == "__main__":
    main()