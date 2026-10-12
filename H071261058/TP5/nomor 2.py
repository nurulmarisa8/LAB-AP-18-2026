ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    indeks = []
    if kata == "":
        return indeks
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    start = 0
    while True:
        i = teks_kecil.find(kata_kecil, start)
        if i == -1:
            break
        indeks.append(i)
        start = i + 1
    return indeks


def cek_batas_kata(teks, i, panjang):
    sebelum_aman = (i == 0) or (teks[i - 1].lower() not in ALFABET)
    j = i + panjang
    sesudah_aman = (j >= len(teks)) or (teks[j].lower() not in ALFABET)
    return sebelum_aman and sesudah_aman


def sensor_kata(teks, kata, simbol):
    if simbol == "":
        simbol = "*"
    simbol = simbol[0]

    indeks_valid = []
    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, len(kata)):
            indeks_valid.append(i)

    hasil = ""
    posisi = 0
    for i in indeks_valid:
        hasil += teks[posisi:i] + simbol * len(kata)
        posisi = i + len(kata)
    hasil += teks[posisi:]

    return (hasil, len(indeks_valid), indeks_valid)


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")
hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)