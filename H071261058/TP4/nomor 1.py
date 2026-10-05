def total(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 90 // 100  
    return subtotal


print("Selamat datang di Kasir Minimarket!")
member = input("Apakah Anda member? (y/n): ")
adalah_member = member == "y"

total_semua = 0
while True:
    nama_barang = str(input("Masukkan nama barang (kosongkan untuk selesai): "))
    if nama_barang == "":
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    subtotal = total(harga, jumlah, adalah_member)
    total_semua += subtotal
    print(f"Subtotal {nama_barang}: Rp{subtotal}")
print(f"Total belanja: Rp{total_semua}")