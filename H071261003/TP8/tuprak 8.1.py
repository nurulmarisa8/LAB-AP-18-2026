import re

def validasi_nim(nim):
    return re.match(r'^H071\d{6}$', nim)

def validasi_email(email):
    return re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email)

def validasi_telepon(telepon):
    return re.match(r'^\d{10,13}$', telepon)

try:
    print("=== Validasi Data Mahasiswa ===")

    nim = input("\nMasukkan NIM        : ")
    email = input("Masukkan Email      : ")
    telepon = input("Masukkan No. Telp : ")

    print("\n--- Hasil Validasi ---")

    if validasi_nim(nim):
        print("NIM        : Valid")
    else:
        print("NIM        : Tidak Valid")

    if validasi_email(email):
        print("Email      : Valid")
    else:
        print("Email      : Tidak Valid")

    if validasi_telepon(telepon):
        print("No. Telepon : Valid")
    else:
        print("No. Telepon : Tidak Valid")

    if (validasi_nim(nim) and validasi_email(email)
            and validasi_telepon(telepon)):
        print("\nData mahasiswa berhasil diverifikasi!")

except Exception as e:
    print("Terjadi kesalahan:", e)
    