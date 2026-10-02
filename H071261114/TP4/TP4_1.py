def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal *= 0.9  # Diskon 10%
    return int(subtotal)

print("Selamat datang di Kasir Minimarket!")
status_input = input("Apakah Anda member? (y/n): ").lower()
is_member = True if status_input == 'y' else False

total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama_barang == "":
        break
    
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    
    subtotal = hitung_subtotal(harga, jumlah, is_member)
    total_belanja += subtotal
    
    print(f"Subtotal {nama_barang}: Rp{subtotal}")

print(f"Total belanja: Rp{total_belanja}")