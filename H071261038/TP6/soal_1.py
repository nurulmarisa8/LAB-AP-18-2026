# Sistem Inventaris Toko Buku (BookNest)

def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil = [buku for buku in inventaris if kata_kunci.lower() in buku["judul"].lower()]
    print(f"\nDitemukan {len(hasil)} buku:")
    for i, buku in enumerate(hasil, 1):
        print(f"{i}. {buku['judul']} - {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")

def update_stok(inventaris, judul, jumlah):
    ditemukan = False
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            ditemukan = True
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print("Pesan gagal: Stok tidak boleh menjadi negatif!")
            else:
                buku["stok"] = stok_baru
                status = "berkurang" if jumlah < 0 else "bertambah"
                print(f"Stok '{buku['judul']}' {status} {abs(jumlah)}. Stok sekarang: {buku['stok']}")
            break
    if not ditemukan:
        print("Pesan error: Buku tidak ditemukan!")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong.")
        return
    
    total_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)
    buku_termahal = max(inventaris, key=lambda x: x["harga"])
    
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah jenis buku : {total_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")
    print(f"Buku termahal     : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("=" * 40)

# Main Program BookNest
def main_booknest():
    inventaris = []
    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_buku(inventaris)
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try:
                harga = float(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif!")
                    continue
                tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Input harga atau stok harus berupa angka!")

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris, kata_kunci)
        
        elif pilihan == "3":
            try:
                judul = input("Judul buku yang ingin diupdate: ")
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Jumlah perubahan harus berupa angka!")

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid")

main_booknest()

