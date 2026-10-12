ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    huruf_kecil =  ch.lower()

    if huruf_kecil in ALFABET:
        posisi = ALFABET.find(huruf_kecil)
        posisi_baru = (posisi + k) % 26
        hasil = ALFABET[posisi_baru]

        if ch == huruf_kecil:
            return hasil

        else:
            return hasil.upper()

    return ch

def mesin_enkripsi(teks, k):
    hasil = ""

    for karakter in teks:
        hasil += cek_sandi(karakter, k)

    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []

    for kunci in range(26):
        pesan_asli = mesin_dekripsi(sandi, kunci)

        if pesan_asli.lower().find(kata_kunci.lower()) != -1:
            hasil.append((kunci, pesan_asli))

    return hasil

try:
    sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
    kata_kunci = input("Masukkan kata kunci target: ")

    if sandi == "":
        raise ValueError("Pesan tersita tidak boleh kosong.")

    if kata_kunci == "":
        raise ValueError("Kata kunci tidak boleh kosong.")

    print()
    print("Output Deskripsi:", retas_sandi(sandi, kata_kunci))

except ValueError as error:
    print("Error:", error)