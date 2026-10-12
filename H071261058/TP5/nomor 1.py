ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for ch in teks:
        if ch in ALFABET or ch in ALFABET.upper():
            hasil += ch
    return hasil.lower()

def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)

def inti_palinrome(teks):
    terpanjang = {
        "teks": "",
        "panjang": 0, 
        "indeks_awal": -1}
    n = len(teks)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks[i:j]
            if len(sub) > terpanjang["panjang"] and cek_palinrome(sub)[0]:
                terpanjang = {"teks": sub, "panjang": len(sub), "indeks_awal": i}
    return terpanjang

teks = input("Masukkan teks prasasti: ")
bersih = bersihkan_teks(teks)
print()
print("Teks Bersih:", bersih)
print("Output Terharap:", inti_palinrome(bersih))