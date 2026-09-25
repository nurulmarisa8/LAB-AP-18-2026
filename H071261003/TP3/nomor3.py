# SISTEM RESERVASI PO BUS


while True :
    try:
        N = int(input("Masukkan jumlah kursi bus: "))
        if N <= 0:
            print("Input Tidak Boleh kurang Dari Nol")
            continue
        break
    except:
        print("input harus berupa angka")
kursi_tersedia = N
total_pendapatan = 0
while kursi_tersedia > 0:
    print("Sisa Kursi", kursi_tersedia)
    try:
        umur = int(input("Masukkan umur penumpang: "))

        if umur < 0:
            print("Umur tidak valid!")
            continue

        if umur <= 5:
            harga = 0

        elif umur <= 12:
            harga = 50000

        else:
            harga = 100000

        total_pendapatan += harga 
        kursi_tersedia -= 1

        print(f"Tiket berhasil diproses. Harga: Rp{harga}")
    except:
        print("Input Umur Harus Berupa Angka")
    
print(f"Total pendapatan: Rp{total_pendapatan}")


# N = int(input("Masukkan jumlah kursi bus: "))
# sisa_kursi = N
# total_pendapatan = 0

# while sisa_kursi > 0:
#     umur = int(input("Masukkan umur penumpang: "))

#     if umur < 0:
#         print("Umur tidak valid!")
#         continue

#     if umur <= 5:
#         harga = 0

#     elif umur <= 12:
#         harga = 50000

#     else:
#         harga = 100000

#     total_pendapatan += harga 
#     sisa_kursi -= 1

#     print(f"Tiket berhasil diproses. Harga: Rp{harga}")
    
# print(f"Total pendapatan: Rp{total_pendapatan}")