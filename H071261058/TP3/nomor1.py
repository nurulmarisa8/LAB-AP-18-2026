print("--- rekapitulasi transaksi dins store ---")
print("ketik'0' untuk menutup toko dan mengakhiri sesi")
while True:
    try:
        dins_store = int(input("Masukkan jumlah item: "))
    except:
        print("input harus berupa angka!")
        continue
    if dins_store == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break
    elif dins_store < 0:
        print("jumlah tidak boleh negatif")
        continue
    elif dins_store > 100 :
        print("maksimal 100 item per transaksi")
        continue
    else:
        print(f"Transaksi {dins_store} item berhasil")
