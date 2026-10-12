ALFABET = "abcdefghijklmnopqrstuvwxyz"
ALFABET_BESAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def bersihkan_teks(teks):
    """Hanya simpan huruf (cek manual ke string alfabet), lalu jadikan huruf kecil."""
    hasil = ""
    for ch in teks:
        if ch in ALFABET or ch in ALFABET_BESAR:
            hasil += ch.lower()
    return hasil


def cek_palinrome(teks):
    """Return (True, -1) jika palindrom, atau (False, indeks_pertama_beda)."""
    terbalik = "".join(reversed(teks))
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)
    return (True, -1)


def inti_palinrome(teks):
    """Cari palindrom terpanjang; jika seri, ambil yang paling kiri."""
    bersih = bersihkan_teks(teks)
    if bersih == "":
        raise ValueError("Teks harus mengandung minimal satu huruf.")
    n = len(bersih)
    terbaik = {"teks": "", "panjang": 0, "indeks_awal": -1}

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = bersih[i:j]
            if len(sub) > terbaik["panjang"] and cek_palinrome(sub)[0]:
                terbaik = {"teks": sub, "panjang": len(sub), "indeks_awal": i}
    return terbaik


if __name__ == "__main__":
    try:
        teks = input("Masukkan teks prasasti: ")

        if teks == "":
            raise ValueError("Teks tidak boleh kosong.")

        hasil = inti_palinrome(teks)

        print()
        print("Teks Bersih:", bersihkan_teks(teks))
        print("Output Terharap:", hasil)
        
    except ValueError as error_input:
        print("Error:", error_input)