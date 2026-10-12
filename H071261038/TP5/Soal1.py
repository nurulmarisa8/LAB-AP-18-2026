# Pembersihan Teks

# 1. Fungsi untuk membersihkan teks dari selain huruf dan mengubah ke huruf kecil
def bersihkan_teks(teks):
    h = ""
    for c in teks.lower():
        if c in "abcdefghijklmnopqrstuvwxyz":
            h = h + c
    return h
# 2. Fungsi untuk mengecek apakah teks adalah palindrom
def cek_palindrom(teks):
    b = "".join(reversed(teks))
    if teks == b:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != b[i]:
            return (False, i)

# 3. Fungsi utama pemcari palindrom terpanjang
def inti_palindrom(teks):
    tb = bersihkan_teks(teks)
    maks, sub_m, idx = 0, "", 0
    for i in range(len(tb)):
        for j in range(i + 1, len(tb) + 1):
            sub = tb[i:j]
            if cek_palindrom(sub)[0] and len(sub) > maks:
                maks, sub_m, idx = len(sub), sub, i
    return {"teks": sub_m, "panjang": maks, "indeks_awal": idx}

# 4. Program utama dengan validasi input agar tidak error
while True:
    m = input("Masukkan teks prasasti: ")
    if any(c.isalnum() for c in m): break
    print("Input harus ada huruf/angka!")

print("Teks Bersih:", bersihkan_teks(m))
print("Output Terharap:", inti_palindrom(m))