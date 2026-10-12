# Brute Force Sandi Caesar Cipher

ALF = "abcdefghijklmnopqrstuvwxyz"

# 1. Fungsi untuk menggeser satu karakter sejauh k posisi
def cek_sandi(ch, k):
    if ch.lower() not in ALF: return ch
    idx = (ALF.find(ch.lower()) + k) % 26
    res = ALF[idx]
    return res.upper() if ch.isupper() else res

# 2. Fungsi enkripsi teks
def mesin_enkripsi(teks, k):
    h = ""
    for c in teks: h = h + cek_sandi(c, k)
    return h

# 3. Fungsi deskripsi (memanggil enkripsi dengan pergeseran negatif)
def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

# 4. Fungsi retas sandi menggunakan metode brute-force (0 sampai 25)
def retas_sandi(sandi, kata_kunci):
    res = []
    for k in range(26):
        p = mesin_dekripsi(sandi, k)
        if p.lower().find(kata_kunci.lower()) != -1:
            res.append((k, p))
    return res

# 5. Program utama dengan validasi input
while True:
    pesan = input("Masukkan pesan tersita: ")
    if pesan.strip(): break
    print("Pesan tidak boleh kosong!")

while True:
    kunci = input("Masukkan kata kunci target: ")
    if kunci.isalpha(): break
    print("Kata kunci harus berupa huruf!")

print("Output Deskripsi:", retas_sandi(pesan, kunci))

    