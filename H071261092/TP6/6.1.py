def tambah_buku(inventaris, judul, penulis, harga, stok):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            print(f"Gagal: Buku dengan judul '{buku['judul']}' sudah ada di inventaris!")
            return False
        
    if harga < 0 or stok < 0:
        print("Gagal: Harga dan stok tidak boleh negatif!")
        return False
    
    buku = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")
    return True

def cari_buku(inventaris, kata_kunci):
    kata_kunci = kata_kunci.lower()
    hasil = []
    for buku in inventaris:
        if kata_kunci in buku["judul"].lower():
            hasil.append(buku)
            
    if hasil:
        print(f"Ditemukan {len(hasil)} buku:")
        nomor = 1 
        for buku in hasil:
            print(f"  {nomor}. {buku['judul']} - {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")
            nomor += 1 
    else:
        print("Buku tidak ditemukan.")


def update_stok(inventaris, judul, jumlah):
    buku_ditemukan = None
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            buku_ditemukan = buku
            break
            
    if not buku_ditemukan:
        print("Error: Buku tidak ditemukan.")
        return
        
    stok_baru = buku_ditemukan["stok"] + jumlah
    if stok_baru < 0:
        print("Gagal: Perubahan membuat stok menjadi negatif.")
    else:
        buku_ditemukan["stok"] = stok_baru
        aksi = "bertambah" if jumlah >= 0 else "berkurang"
        print(f"Stok '{buku_ditemukan['judul']}' {aksi} {abs(jumlah)}. Stok sekarang: {stok_baru}")

def ringkasan_inventaris(inventaris):
    print("========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    
    jumlah_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)
    
    print(f"Jumlah jenis buku  : {jumlah_jenis}")
    print(f"Total seluruh stok : {total_stok}")
    print(f"Total nilai aset   : Rp{total_aset}")
    
    if inventaris:
        buku_termahal = max(inventaris, key=lambda x: x["harga"])
        print(f"Buku termahal      : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    else:
        print("Buku termahal      : Belum ada buku")
    print("========================================")

def main():
    inventaris_buku = []
    
    while True:
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            judul = input("Judul buku: ")
            penulis = input("Penulis: ")
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                tambah_buku(inventaris_buku, judul, penulis, harga, stok)
            except ValueError:
                print("Gagal: Harga dan stok harus berupa angka!")
                
        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            cari_buku(inventaris_buku, kata_kunci)
            
        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                update_stok(inventaris_buku, judul, jumlah)
            except ValueError:
                print("Gagal: Jumlah perubahan harus berupa angka!")
                
        elif pilihan == "4":
            ringkasan_inventaris(inventaris_buku)
            
        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-5.")

if __name__ == "__main__":
    main()