def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }

    inventaris.append(buku)


def cari_buku(inventaris, kata_kunci):
    hasil = []

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)

    return hasil


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal: stok tidak mencukupi.")
                return

            buku["stok"] = stok_baru

            if jumlah > 0:
                print(
                    f"Stok '{buku['judul']}' bertambah {jumlah}. "
                    f"Stok sekarang: {stok_baru}"
                )
            elif jumlah < 0:
                print(
                    f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. "
                    f"Stok sekarang: {stok_baru}"
                )
            else:
                print("Stok tidak mengalami perubahan.")

            return

    print("Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0

    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]

    print("\n===== RINGKASAN INVENTARIS =====")
    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset:,.0f}".replace(",", "."))

    if len(inventaris) > 0:
        buku_termahal = inventaris[0]

        for buku in inventaris:
            if buku["harga"] > buku_termahal["harga"]:
                buku_termahal = buku

        harga = f"{buku_termahal['harga']:,.0f}".replace(",", ".")
        print(
            f"Buku termahal     : {buku_termahal['judul']} "
            f"(Rp{harga})"
        )
    else:
        print("Buku termahal     : Belum ada buku")

    print("=" * 33)


inventaris = []

print("========================================")
print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("========================================")

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    try:
        pilihan = int(input("Pilih menu (1-5): "))
    except ValueError:
        print("Error: pilihan menu harus berupa angka.")
        continue

    if pilihan == 1:
        judul = input("Judul buku: ").strip()
        penulis = input("Penulis: ").strip()

        if judul == "" or penulis == "":
            print("Error: judul dan penulis tidak boleh kosong.")
            continue

        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Error: harga dan stok tidak boleh negatif.")
                continue

        except ValueError:
            print("Error: harga harus berupa angka dan stok harus bilangan bulat.")
            continue

        tambah_buku(inventaris, judul, penulis, harga, stok)
        print(f"Buku '{judul}' berhasil ditambahkan!")

    elif pilihan == 2:
        kata_kunci = input("Masukkan kata kunci judul: ").strip()

        hasil = cari_buku(inventaris, kata_kunci)

        if len(hasil) > 0:
            print(f"Ditemukan {len(hasil)} buku:")

            for nomor, buku in enumerate(hasil, start=1):
                print(
                    f"  {nomor}. {buku['judul']} - {buku['penulis']} "
                    f"| Rp{buku['harga']:g} | Stok: {buku['stok']}"
                )
        else:
            print("Buku tidak ditemukan.")

    elif pilihan == 3:
        judul = input("Judul buku yang ingin diupdate: ").strip()

        try:
            jumlah = int(
                input(
                    "Jumlah perubahan (positif=tambah, negatif=kurang): "
                )
            )
        except ValueError:
            print("Error: jumlah perubahan harus berupa bilangan bulat.")
            continue

        update_stok(inventaris, judul, jumlah)

    elif pilihan == 4:
        ringkasan_inventaris(inventaris)

    elif pilihan == 5:
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak tersedia. Masukkan angka 1-5.")