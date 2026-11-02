import re

try:
    print("=== Pembersihan Data Nomor Telepon ===")

    jumlah = int(input("Masukkan jumlah data: "))

    data = []
    data_bersih = []
    data_valid = []

    for i in range(jumlah):
        nomor = input(f"\nNomor ke-{i+1}: ")
        data.append(nomor)

    print("\n--- Hasil Pembersihan ---")

    for i, nomor in enumerate(data, start=1):
        bersih = re.sub(r'[\s-]', '', nomor)
        data_bersih.append(bersih)

        if (re.match(r'^[\d -]+$', nomor)
                and re.match(r'^\d{10,13}$', bersih)):
            status = "Valid"
            data_valid.append(bersih)
        else:
            status = "Tidak valid"

        print(f"\nData {i}:")
        print("Sebelum :", nomor)
        print("Sesudah :", bersih)
        print("Status  :", status)

    print("\nJumlah nomor valid:", len(data_valid))

except ValueError:
    print("Jumlah data harus berupa angka!")

except Exception as e:
    print("Terjadi kesalahan:", e)