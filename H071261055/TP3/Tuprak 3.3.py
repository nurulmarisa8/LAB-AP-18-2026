# Sistem reservasi "po bus"

while True:
    try:
        jumlah_kursi = int(input("masukkan maksimal kursi bus: "))
        break
    except ValueError:
        print("input jumlah kursi harus berupa angka!")

sisa_kursi = jumlah_kursi
total_pendapatan = 0

# sistem reservasi po bus dimulai

while sisa_kursi > 0:
    print(f"sisa kursi: {sisa_kursi}")
    try:
        umur = int(input("masukkan umur penumpang: "))

        if umur < 0:
            print("umur tidak valid!")
            continue

    except ValueError:
        print("input umur harus berupa angka!")
        continue
    if umur <= 5:
        kategori =  "balita"
        harga = 0

    elif umur <= 12:
        kategori = "anak"
        harga = 50000

    else:
        kategori = "dewasa"
        harga = 100000

    print(f"kategori: {kategori} - harga: Rp {harga:,}".replace(",", "."))

    sisa_kursi -= 1
    total_pendapatan += harga

# semua kursi terisi

print(f"total pendapatan perjalanan po bus kali ini: Rp {total_pendapatan:,}".replace(",", "."))