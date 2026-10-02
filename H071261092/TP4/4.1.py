print("selamat datang di kasir minimarket")
def hitung_subtotal(harga, jumlah, adalah_member):
    subtotal = harga * jumlah 
    if adalah_member:
        subtotal *= 0.9  
    return subtotal
print("selamat datang di minimarket")
status_member = input("apakah anda member? (y/n): ")
adalah_member = True if status_member == 'y' else False

total_belanja = 0
while True:
    nama_barang = input("masukkan nama barang (atau 'kosongkan' untuk mengakhiri): ")
    if nama_barang == "":
        break
    harga = float(input("masukkan harga barang: "))
    jumlah = int(input("masukkan jumlah barang: "))
    subtotal = hitung_subtotal(harga, jumlah, adalah_member)
    total_belanja += subtotal
    print(f"Subtotal untuk {nama_barang}: Rp. {subtotal}")

print(f"Total belanja: Rp. {total_belanja}")