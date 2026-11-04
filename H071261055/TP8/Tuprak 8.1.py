import re

def validasi_nim(nim):
    if not re.fullmatch(r"H071\d{6}", nim):
        raise ValueError("Format NIM tidak valid!")
    return nim

def validasi_email(email):
    pola = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
    if not re.fullmatch(pola, email):
        raise ValueError("Format email tidak valid!")
    return email

def validasi_telepon(telp):
    if not re.fullmatch(r"\d{10,13}", telp):
        raise ValueError("Nomor telepon tidak valid!")
    return telp

def jalankan_validasi(validator, nilai):
    try:
        validator(nilai)
        return True, "Valid"
    except ValueError as pesan_error:
        return False, str(pesan_error)

print("=== Validasi Data Mahasiswa ===\n")
nim = input("Masukkan NIM       : ").strip()
email = input("Masukkan Email     : ").strip()
telp = input("Masukkan No. Telp   : ").strip()

nim_ok, pesan_nim = jalankan_validasi(validasi_nim, nim)
email_ok, pesan_email = jalankan_validasi(validasi_email, email)
telp_ok, pesan_telp = jalankan_validasi(validasi_telepon, telp)

print("\n--- Hasil Validasi ---")
print("NIM         :", pesan_nim)
print("Email       :", pesan_email)
print("No. Telepon :", pesan_telp)

if nim_ok and email_ok and telp_ok:
    print("\nData mahasiswa berhasil diverifikasi!")