import re

def validasi_username(username):
    return re.match(r'^[A-Za-z][A-Za-z0-9_]{4,11}$', username)

try:
    daftar_username = []

    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.")

    while True:
        username = input("\nMasukkan username: ")

        if username == "SELESAI":
            break

        if validasi_username(username):
            print("Username tersedia.")
            daftar_username.append(username)
        else:
            print("Username tidak valid!")

    print("\n=== Rekapitulasi ===")
    print("Username valid:")

    for i, username in enumerate(daftar_username, start=1):
        print(f"{i}. {username}")

    print("\nJumlah username valid:", len(daftar_username))

except Exception as e:
    print("Terjadi kesalahan:", e)