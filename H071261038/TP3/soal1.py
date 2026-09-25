# Rekapitulasi Transaksi Dins Store

print("--- Rekapitulasi Transaksi Dins Store ---")
print ("Ketik '0' untuk menutup toko dan mengakhiri sesi")

while True:
    try: 
        jumlah = int(input("Masukkan jumlah item: "))
    except: 
        print("input harus berupa angka!")
        continue

    if jumlah == 0:
        print("Toko ditutup. Sesi rekap selesai")
        break
    elif jumlah < 0:
        print ("Jumlah tak boleh negatif")
    elif jumlah > 100:
        print("Maksimal 100 item per transaksi")
    else:
        print("Transaksi {jumlah} item berhasil!")

