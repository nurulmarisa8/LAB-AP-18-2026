import re

def validasi_username(username):
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11}", username):
        raise ValueError("Username tidak valid!")
    return username

username_valid = []

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.\n")

while True:
    username = input("Masukkan username: ").strip()

    if username == "SELESAI":
        break

    try:
        validasi_username(username)
        username_valid.append(username)
        print("Username tersedia.\n")
    except ValueError as pesan_error:
        print(f"{pesan_error}\n")

print("\n=== Rekapitulasi ===")
print("Username valid:")
for no, nama in enumerate(username_valid, start=1):
    print(f"{no}. {nama}")

print(f"\nJumlah username valid: {len(username_valid)}")