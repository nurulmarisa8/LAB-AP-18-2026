def hitung_subtotal (harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah

    if adalah_member :
        subtotal = round(subtotal * 0.9) 
        
    return subtotal

print("Selamat datang di Kasir Minimarket!")
status_member = input("Apakah Anda member? (y/n): ")

if status_member =="y":
    adalah_member = True
else:
    adalah_member = False

total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break

    harga = int(input("Harga barang:"))
    jumlah = int(input("Jumlah barang: "))
    subtotal = hitung_subtotal(harga, jumlah, adalah_member)

    print(f"Subtotal {nama_barang}: Rp{subtotal}")


    total += subtotal

print(f"Total belanja: Rp{total}")

