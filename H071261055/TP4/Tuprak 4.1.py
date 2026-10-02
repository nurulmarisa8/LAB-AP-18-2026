def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = round(subtotal * 0.9)  

    return subtotal

print("Selamat Datang di Kasir Minimarket!")

status_member = input("Apakah Anda adalah member? (y/n): ").lower() 

while True:
    nama_barang = input("masukkan nama barang (kosongkan untuk selesai): ")
    if  nama_barang == "":
        break
    harga = int(input("harga barang: "))
    jumlah = int(input("jumlah barang: "))
    subtotal = hitung_subtotal(harga, jumlah, status_member == "y")

    print(f"Subtotal untuk {nama_barang}: {subtotal}")

    if "total" not in locals():
        total = 0
    total += subtotal

print(f"Total belanja: {total}")