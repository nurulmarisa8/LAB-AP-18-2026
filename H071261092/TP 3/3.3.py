while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))
        if N <= 0:
            print("Jumlah kursi harus lebih dari 0!")
        else:
            sisa_kursi = N
            total_pendapatan = 0
        
            print("Sistem Reservasi PO BUS Dimulai")
            print(f"Sisa kursi: {sisa_kursi}")
        
            while sisa_kursi > 0:
                try:
                    umur = int(input("Masukkan umur penumpang: "))
                
                    if umur < 0:
                        print("Umur tidak valid!")
                        print(f"Sisa kursi: {sisa_kursi}")
                        continue
                
                    if umur <= 5:
                        sisa_kursi -= 1
                        harga = 0
                        print("Kategori: Balita")
                        print(f"Sisa kursi: {sisa_kursi}")
                        print("Tiket Gratis (Rp 0)")
                    elif umur <= 12:
                        sisa_kursi -= 1
                        harga = 50000
                        print(f"Kategori: Anak Harga: Rp {harga:,}".replace(',', '.'))
                        print(f"Sisa kursi: {sisa_kursi}")
                    else:
                        sisa_kursi -= 1
                        harga = 100000
                        print(f"Kategori: Dewasa Harga: Rp {harga:,}".replace(',', '.'))
                        print(f"Sisa kursi: {sisa_kursi}")
                
                    total_pendapatan += harga
                
                except:
                    print("Input umur harus berupa angka!")
                    print(f"Sisa kursi: {sisa_kursi}")
                
        print("Semua Kursi Terisi")
        print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan:,}".replace(',', '.'))

    except:
        print("Input jumlah kursi harus berupa angka!")