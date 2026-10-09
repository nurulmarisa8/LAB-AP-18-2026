ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for ch in teks:
        kecil = ch.lower()
        if kecil in ALFABET:
            hasil += kecil
    return hasil


def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for posisi in range(len(teks)):
        if teks[posisi] != terbalik[posisi]:
            return (False, posisi)


def inti_palinrome(teks):
    terbaik = {"teks": "", "panjang": 0, "indeks_awal": -1}
    n = len(teks)
    for awal in range(n):
        for akhir in range(awal + 1, n + 1):
            sub = teks[awal:akhir]
            if len(sub) > terbaik["panjang"] and cek_palinrome(sub)[0]:
                terbaik = {"teks": sub, "panjang": len(sub), "indeks_awal": awal}
    return terbaik


while True:
    teks = input("Masukkan teks prasasti: ")
    if teks == "":
            break
    bersih = bersihkan_teks(teks)
    print("Teks Bersih:", bersih)
    print("Output Terharap:", inti_palinrome(bersih))