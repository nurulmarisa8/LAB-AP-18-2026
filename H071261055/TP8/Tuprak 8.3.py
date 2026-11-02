import re

def bersihkan_nomor(nomor):
    return re.sub(r"[ -]", "", nomor)

def validasi_telepon(nomor_bersih):
    if not re.fullmatch(r"\d{10,13}", nomor_bersih):
        raise ValueError("Nomor telepon tidak valid!")
    return nomor_bersih

def minta_jumlah():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah data: "))
            if jumlah <= 0:
                raise ValueError("Jumlah harus lebih dari 0")
            return jumlah
        except ValueError:
            print("Input tidak valid! Masukkan bilangan bulat lebih dari 0.\n")

print("=== Pembersihan Data Nomor Telepon ===\n")
jumlah = minta_jumlah()

data_sebelum = []
data_sesudah = []
status_data = []
nomor_valid = []

for i in range(1, jumlah + 1):
    nomor = input(f"\nNomor ke-{i}: ").strip()
    bersih = bersihkan_nomor(nomor)

    data_sebelum.append(nomor)
    data_sesudah.append(bersih)

    try:
        validasi_telepon(bersih)
        nomor_valid.append(bersih)
        status_data.append("Valid")
    except ValueError:
        status_data.append("Tidak valid")

print("\n--- Hasil Pembersihan ---")
for i in range(jumlah):
    print(f"\nData {i + 1}:")
    print(f"Sebelum : {data_sebelum[i]}")
    print(f"Sesudah : {data_sesudah[i]}")
    print(f"Status  : {status_data[i]}")

print(f"\nJumlah nomor valid: {len(nomor_valid)}")