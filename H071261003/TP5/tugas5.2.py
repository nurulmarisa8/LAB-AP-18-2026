ALFABET = "abcdefghijklmnopqrstuvwxyz" 

def cek_kata(teks, kata):
    indeks = []

    mulai = 0
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    while True:
        posisi = teks_kecil.find(kata_kecil, mulai)

        if posisi == -1:
            break

        indeks.append(posisi)
        mulai = posisi + 1

    return indeks

def cek_batas_kata(teks, i, panjang):
    if i > 0:
        sebelum = teks[i - 1].lower()

        if sebelum in ALFABET:
            return False

    posisi_akhir = i + panjang

    if posisi_akhir < len(teks):
        sesudah = teks[posisi_akhir].lower()

        if sesudah in ALFABET:
            return False

    return True

def sensor_kata(teks, kata, simbol):
    semua_indeks = cek_kata(teks, kata)

    indeks_valid = []

    for i in semua_indeks:
        if cek_batas_kata(teks, i, len(kata)):
            indeks_valid.append(i)

    hasil = ""
    awal = 0

    for i in indeks_valid:
        hasil += teks[awal:i]
        hasil += simbol * len(kata)

        awal = i + len(kata)

    hasil += teks[awal:]
    return hasil, len(indeks_valid), indeks_valid  

try:
    teks = input("Masukkan Teks: ")
    kata = input("Masukkan kata target: ")
    simbol = input("Masukkan simbol: ")

    if teks == "":
        raise ValueError("Teks tidak boleh kosong.")

    if kata == "":
        raise ValueError("Kata target tidak boleh kosong.")

    if simbol == "":
        raise ValueError("Simbol tidak boleh kosong.") 

    if len(simbol) != 1:
        raise ValueError("Simbol harus berupa satu karakter.")

    hasil = sensor_kata(teks, kata, simbol)


    print("Hasil Teks:", hasil[0])
    print("Jumlah:", hasil[1], "| Indeks:", hasil[2])

except ValueError as error:
    print("Error:", error)