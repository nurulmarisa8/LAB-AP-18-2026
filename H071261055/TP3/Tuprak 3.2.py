# Denah Kursi Bioskop

while True:
    try:
        jumlah_baris = int(input("masukkan jumlah baris:  "))

        if jumlah_baris <= 0:
            print("jumlah baris harus lebih dari 0!")
        else:
            break

    except ValueError:
        print("input baris harus berupa angka!")

while True:
    try:
        jumlah_kursi = int(input("masukkan jumlah kursi per baris: "))

        if jumlah_kursi <= 0:
            print("jumlah kursi harus lebih dari 0!")
        else:
            break

    except ValueError:
        print("input kursi harus berupa angka!")

# Daftar kursi tersedia

for baris in range(1, jumlah_baris + 1):
    for kursi in range(1, jumlah_kursi + 1):
        if kursi == 13:
            continue
        if baris == 1:
            if kursi % 2 == 0:
                continue

        print(f"baris {baris} - kursi {kursi}")