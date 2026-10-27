inventaris_toko = []

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok,
    }
    inventaris.append(buku)
    print()
    print(f"Buku '{judul}' berhasil ditambahkan!")
    print()

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
    print(f"Ditemukan {len(hasil)} buku:")
    for i in range(len(hasil)):
        buku = hasil[i]
        print(f"  {i + 1}. {buku['judul']} - {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if jumlah < 0:
                buku["stok"] = stok_baru
                print(f"Stok '{buku['judul']}' berkurang {-jumlah}. Stok sekarang: {buku['stok']}")
            else:
                buku["stok"] = stok_baru
                print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {buku['stok']}")
            return
    print("Buku yang anda masukkan tidak ada")

def ringkasan_inventaris(inventaris):
    if len(inventaris) == 0:
        print("Inventaris masih kosong.")
        return
    total_buku = len(inventaris)
    total_seluruh_stok = 0
    total_nilai_aset = 0
    buku_tertinggi = None
    harga_tertinggi = 0
    for i in inventaris:
        total_seluruh_stok += i["stok"]
        total_nilai_aset += i["harga"] * i["stok"]
        if i["harga"] > harga_tertinggi:
            buku_tertinggi = i["judul"]
            harga_tertinggi = i["harga"]
    print()
    print("===================================")
    print("  RINGKASAN INVENTARIS BOOKNEST")
    print("===================================")
    print(f"Jumlah jenis buku : {total_buku}")
    print(f"Total seluruh stok: {total_seluruh_stok}")
    print(f"Total nilai aset  : Rp{total_nilai_aset}")
    print(f"Buku termahal     : {buku_tertinggi} (Rp{harga_tertinggi})")
    print("===================================")

print()
print("=======================================")
print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=======================================")
while True:
    print()
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
    try:
        menu = int(input("Pilih menu (1-5): "))
    except ValueError:
        print("Input yang anda masukkan tidak valid")
        continue

    if menu == 1:
        judul_buku = input("Judul buku: ").title()
        penulis = input("Penulis: ").title()
        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
        except ValueError:
            print("Harga dan stok harus berupa angka")
            continue
        if harga < 0 or stok < 0:
            print("Harga atau stok tidak boleh negatif")
            continue
        tambah_buku(inventaris_toko, judul_buku, penulis, harga, stok)
    elif menu == 2:
        mencari_buku = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris_toko, mencari_buku)
    elif menu == 3:
        judul_buku = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah_perubahan = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
        except ValueError:
            print("Jumlah perubahan harus berupa angka")
            continue
        update_stok(inventaris_toko, judul_buku, jumlah_perubahan)
    elif menu == 4:
        ringkasan_inventaris(inventaris_toko)
    elif menu == 5:
        print("Terima kasih telah menggunakan BookNest!")
        break
    else:
        print("Input yang anda masukkan tidak valid")