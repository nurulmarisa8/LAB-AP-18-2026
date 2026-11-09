import re

def validasi_nim(nim):
    pattern = r'^H071\d{6}$'
    return bool(re.match(pattern, nim))

def validasi_email(email):
    pattern = r'^\w+[\w.-]*@[\w.-]+\.[\w]+$'
    return bool(re.match(pattern, email))

def validasi_telepon(telepon):
    pattern = r'[0-9]{10,13}$'
    return bool(re.match(pattern, telepon))

def main():
    print("=== Validasi Data Mahasiswa ===")
    print()
    
    nim = input("Masukkan NIM       : ")
    email = input("Masukkan Email     : ")
    telepon = input("Masukkan No. Telp  : ")
    
    nim_valid = validasi_nim(nim)
    email_valid = validasi_email(email)
    telp_valid = validasi_telepon(telepon)
    
    print("\n--- Hasil Validasi ---")
    
    if nim_valid:
        print("NIM          : Valid")
    else:
        print("NIM          : Tidak Valid")
        
    if email_valid:
        print("Email        : Valid")
    else:
        print("Email        : Tidak Valid")
        
    if telp_valid:
        print("No. Telepon  : Valid")
    else:
        print("No. Telepon  : Tidak Valid")
        
    print()
    
    if nim_valid and email_valid and telp_valid:
        print("Data mahasiswa berhasil diverifikasi!")
    else:
        print("Data mahasiswa gagal diverifikasi!")

if __name__ == "__main__":
    main()
