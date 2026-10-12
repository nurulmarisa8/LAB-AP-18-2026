ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    """Geser satu karakter sejauh k (boleh negatif / > 26). Non-huruf tidak diubah."""
    idx = ALFABET.find(ch.lower())
    if idx == -1:
        return ch
    baru = ALFABET[(idx + k) % 26]
    if ch == ch.upper():
        return baru.upper()
    return baru.lower()


def mesin_enkripsi(teks, k):
    hasil = ""
    for ch in teks:
        hasil += cek_sandi(ch, k)
    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    """Brute force kunci 0-25, simpan yang mengandung kata kunci."""
    if sandi == "":
        raise ValueError("Pesan tersita tidak boleh kosong.")
    if kata_kunci == "":
        raise ValueError("Kata kunci tidak boleh kosong.")

    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil


if __name__ == "__main__":
    try:
        sandi = input("Masukkan pesan tersita: ")
        kunci = input("Masukkan kata kunci target: ")

        hasil = retas_sandi(sandi, kunci)

        if len(hasil) == 0:
            raise ValueError("Tidak ada pergeseran yang menghasilkan kata kunci tersebut.")

        print()
        print("Output Deskripsi:", hasil)

    except ValueError as error_input:
        print("Error:", error_input)