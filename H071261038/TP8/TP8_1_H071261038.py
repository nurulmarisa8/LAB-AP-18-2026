# Validasi Data Mahasiswa

import re

def validasi_nim(nim):
    pattern = r'^H071\d{6}$'
    return bool(re.match(pattern, nim))

def validasi_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validasi_telepon(telepon):
    pattern = r'^\d{10,13}$'
    return bool(re.match(pattern, telepon))

def main():
    print("=== Validasi Data Mahasiswa ===")
    nim = input("Masukkan NIM           : ")
    email = input("Masukkan Email         : ")
    telp = input ("Masukkan Nomor Telepon : ")

    print(" --- Hasil Validasi ---")
    is_nim_valid = validasi_nim(nim)
    is_email_valid = validasi_email(email)
    is_telp_valid = validasi_telepon(telp)

    # Validasi NIM
    if validasi_nim(nim):
        print("NIM      : Valid")
    else: 
        print("NIM      : Format NIM Tidak Valid")

    # Validasi Email
    if validasi_email(email):
        print("Email    : Valid")
    else:
        print("Email    : Format Email Tidak Valid")

    # Validasi No. Telepon
    if validasi_telepon(telp):
        print("No. Telp : Valid")
    else:
        print("No. Telp : Nomor Telepon Tidak Valid")

    if is_nim_valid and is_email_valid and is_telp_valid:
        print("\nData Mahasiswa Berhasil Diverivikasi!")
    else:
        print("\n Data mahasiswa tidak berhasil diverifikasi")


main()
