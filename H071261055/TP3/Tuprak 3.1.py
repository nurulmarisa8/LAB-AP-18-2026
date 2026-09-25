# Rekapitulasi Transaksi "Dins Store"

while True:
    try:
        jumlah = int(input("masukkan jumlah item: "))
        if jumlah == 0:
            print("toko ditutup. sesi rekap selesai.")
            break
        elif jumlah < 0:
            print("jumlah tidak boleh negatif")
        elif jumlah > 100:
            print("maksimal 100 item per transaksi!")
        else:
            print(f"transaksi {jumlah} item berhasil!")
    except ValueError:
        print("input harus berupa angka!")