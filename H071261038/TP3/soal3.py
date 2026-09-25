# Validasi input kuota awal kursi bus
while True:
    try:
        sisa_kursi = int(input("Masukkan maksimal kursi bus: "))
        if sisa_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except:
        print("Input jumlah kursi harus berupa angka!")
        print("--- Sistem Reservasi PO BUS Dimulai ---")

    total_pendapatan = 0

# Perulangan while berjalan selama sisa_kursi > 0

while sisa_kursi > 0:
    print(f"Sisa kursi: {sisa_kursi}")

    try:
        umur = int(input("Masukkan umur penumpang: "))
    except:
        print("Input umur harus berupa angka!")
        continue

    # Validasi input umur negatif
    if umur < 0:
        print("Umur tidak valid!")
        continue

    # Penentuan harga tiket
    if 0 <= umur <= 5:
        kategori = "Balita"
        harga = 0
        print(f"kategori: {kategori} - Tiket gratis (Rp {harga})")

    elif 6<= umur <= 12:
        kategori = "Anak"
        harga = 50000
        print(f"kategori: {kategori} - harga {harga}")

    else:
        kategori = "Dewasa"
        harga = 100000
        print(f"kategori: {kategori} - harga {harga}")

    # Total Pendapatan dan Pengurangan Sisa Kursi
    total_pendapatan += harga
    sisa_kursi -= 1

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS: Rp {total_pendapatan}")
