ALFABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cek_kata(teks, kata):
    """Return list semua indeks kemunculan kata (tidak peka huruf besar/kecil)."""
    hasil = []
    if kata == "":
        return hasil
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    start = 0
    while True:
        i = teks_kecil.find(kata_kecil, start)
        if i == -1:
            break
        hasil.append(i)
        start = i + 1
    return hasil


def cek_batas_kata(teks, i, panjang):
    """True jika karakter sebelum & sesudah kata bukan huruf (atau batas teks)."""
    sebelum_ok = (i == 0) or (teks[i - 1] not in ALFABET)
    j = i + panjang
    sesudah_ok = (j >= len(teks)) or (teks[j] not in ALFABET)
    return sebelum_ok and sesudah_ok


def sensor_kata(teks, kata, simbol):
    """Return (teks_tersensor, jumlah_tersensor, list_indeks_awal)."""
    if teks == "":
        raise ValueError("Teks tidak boleh kosong.")
    if kata == "":
        raise ValueError("Kata target tidak boleh kosong.")
    if simbol == "":
        raise ValueError("Simbol tidak boleh kosong.")

    simbol = simbol[0]  
    panjang = len(kata)

    hasil = ""
    indeks_sensor = []
    posisi = 0  

    for i in cek_kata(teks, kata):
        if cek_batas_kata(teks, i, panjang):
            hasil = hasil + teks[posisi:i] + simbol * panjang
            posisi = i + panjang
            indeks_sensor.append(i)

    hasil = hasil + teks[posisi:]
    return (hasil, len(indeks_sensor), indeks_sensor)


if __name__ == "__main__":
    try:
        teks = input("Masukkan Teks: ")
        kata = input("Masukkan kata target: ")
        simbol = input("Masukkan simbol: ")

        hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
        print("Hasil Teks:", hasil)
        print("Jumlah:", jumlah, "| Indeks:", indeks)
        
    except ValueError as error_input:
        print("Error:", error_input)