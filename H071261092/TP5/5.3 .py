ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch,k):
    indeks = ALFABET.find(ch.lower())
    if indeks == -1:
        return ch
    indeks_baru = (indeks + k) % 26
    if ch.isupper():
        return ALFABET[indeks_baru].upper()
    return ALFABET[indeks_baru].lower()

def mesin_enkripsi(teks,k): 
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch,k)
    return hasil

def mesin_dekripsi(teks,k):
    return mesin_enkripsi(teks,-k)

def retas_sandi(sandi,kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi,k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k,pesan))
    return hasil

while True:
    teks = input("masukkan pesan tersita (enkripsi caesar): ")
    if teks == "":
        break
    kata_kunci = input("masukkan kata kunci: ")
    if  kata_kunci == "":
        break
    hasil = retas_sandi(teks,kata_kunci)
    print("Output Deskripsi : ", hasil)