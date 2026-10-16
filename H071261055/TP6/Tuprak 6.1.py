def baca_angka(prompt, nama):
    """Membaca input angka bulat. Jika bukan angka -> ValueError."""
    try:
        return int(input(prompt))
    except ValueError:
        raise ValueError(f"{nama} harus berupa angka!") from None


def tambah_buku(inventaris, judul, penulis, harga, stok):
    if judul.strip() == "" or penulis.strip() == "":
        raise ValueError("Judul dan penulis tidak boleh kosong!")
    if harga < 0 or stok < 0:
        raise ValueError("Harga dan stok tidak boleh negatif!")
    inventaris.append({
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok,
    })
    print(f"Buku '{judul}' berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    if kata_kunci.strip() == "":
        raise ValueError("Kata kunci tidak boleh kosong!")
    kata_kunci = kata_kunci.lower()
    hasil = [b for b in inventaris if kata_kunci in b["judul"].lower()]
    if not hasil:
        print("Tidak ada buku yang cocok.")
        return
    print(f"Ditemukan {len(hasil)} buku:")
    for i, b in enumerate(hasil, 1):
        print(f" {i}. {b['judul']} - {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")


def update_stok(inventaris, judul, jumlah):
    for b in inventaris:
        if b["judul"].lower() == judul.lower():
            stok_baru = b["stok"] + jumlah
            if stok_baru < 0:
                raise ValueError(f"Gagal! Stok '{b['judul']}' tidak mencukupi "
                                 f"(stok saat ini: {b['stok']}).")
            b["stok"] = stok_baru
            if jumlah >= 0:
                print(f"Stok '{b['judul']}' bertambah {jumlah}. Stok sekarang: {b['stok']}")
            else:
                print(f"Stok '{b['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {b['stok']}")
            return
    raise ValueError(f"Buku '{judul}' tidak ditemukan!")


def ringkasan_inventaris(inventaris):
    if not inventaris:
        raise ValueError("Inventaris masih kosong!")
    total_stok = sum(b["stok"] for b in inventaris)
    total_aset = sum(b["harga"] * b["stok"] for b in inventaris)
    termahal = max(inventaris, key=lambda b: b["harga"])
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah jenis buku : {len(inventaris)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    print(f"Buku termahal : {termahal['judul']} (Rp{termahal['harga']})")
    print("=" * 40)


def main():
    inventaris = []
    print("=" * 40)
    print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("=" * 40)

    while True:
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        try:
            pilihan = baca_angka("Pilih menu (1-5): ", "Pilihan menu")

            if pilihan == 1:
                judul = input("Judul buku: ")
                penulis = input("Penulis: ")
                harga = baca_angka("Harga: ", "Harga")
                stok = baca_angka("Stok awal: ", "Stok")
                tambah_buku(inventaris, judul, penulis, harga, stok)
            elif pilihan == 2:
                kata_kunci = input("Masukkan kata kunci judul: ")
                cari_buku(inventaris, kata_kunci)
            elif pilihan == 3:
                judul = input("Judul buku yang ingin diupdate: ")
                jumlah = baca_angka("Jumlah perubahan (positif=tambah, negatif=kurang): ",
                                    "Jumlah perubahan")
                update_stok(inventaris, judul, jumlah)
            elif pilihan == 4:
                ringkasan_inventaris(inventaris)
            elif pilihan == 5:
                print("Terima kasih telah menggunakan BookNest!")
                break
            else:
                raise ValueError("Pilihan menu harus antara 1 sampai 5!")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()