# Kasir Minimarket (Default Parameter)

def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal *= 0.9
    return int(subtotal)

def main_kasir():
    print("Selamat datang di Kasir Minimarket")
    status = input("Apakah Anda member? (y/n): ")
    is_member = True if status == 'y' else False

    total_belanja = 0

    while True:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if nama_barang == "":
            break

        harga = int(input("Harga barang: "))
        jumlah = int(input("Jumlah barang: "))

        subtotal = hitung_subtotal(harga, jumlah, adalah_member=is_member)
        total_belanja += subtotal

        print(f"Subtotal {nama_barang}: Rp{subtotal}")

    print(f"Total belanja: Rp{total_belanja}")

if __name__== "__main__":
    main_kasir()