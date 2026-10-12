
ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""

    for karakter in teks:
        karakter_kecil = karakter.lower()

        if karakter_kecil in ALFABET:
            hasil += karakter_kecil

    return hasil

def cek_palinrome(teks):
    teks_balik = "".join(reversed(teks))

    if teks == teks_balik:
        return True, -1

    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return False, i

    return False, -1

def inti_palinrome(teks):
    teks_bersih = bersihkan_teks(teks)

    if teks_bersih == "":
        return {
            "teks": "",
            "panjang": 0,
            "indeks_awal": -1
        }

    palindrom_terpanjang = ""
    indeks_awal = 0

    for i in range(len(teks_bersih)):   
        for j in range(i + 1, len(teks_bersih) + 1):
            substring = teks_bersih[i:j]

            hasil = cek_palinrome(substring)

            if hasil[0] :
                if len(substring) > len(palindrom_terpanjang):
                    palindrom_terpanjang = substring
                    indeks_awal = i
    return {
        "teks": palindrom_terpanjang,
        "panjang": len(palindrom_terpanjang),
        "indeks_awal": indeks_awal
    }
try:
    teks = input("Masukkan teks prasasti: ")

    if teks == "":
        raise ValueError("Teks tidak boleh kosong.")

    teks_bersih = bersihkan_teks(teks)

    if teks_bersih == "":
        raise ValueError ("Teks tidak mengandung huruf alfabet.")
    

    hasil = inti_palinrome(teks)

    print ()
    print("Teks bersih:", teks_bersih)
    print("Output Terharap:", hasil)

except ValueError as error:
    print("Error:", error)
