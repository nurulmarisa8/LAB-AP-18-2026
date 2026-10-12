ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    ch_lower = ch.lower()
    idx = ALFABET.find(ch_lower)
    
    # Jika karakter bukan merupakan huruf alfabet
    if idx == -1:
        return ch
        
    # Perhitungan pergeseran dengan modulus 26
    new_idx = (idx + k) % 26
    new_char = ALFABET[new_idx]
    
    if ch.isupper():
        return new_char.upper()
    else:
        return new_char

def mesin_enkripsi(teks, k):
    hasil = ""
    for char in teks:
        hasil += cek_sandi(char, k)
    return hasil

def mesin_dekripsi(teks, k):
    # Memanggil mesin_enkripsi dengan k berlawanan arah
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil_retas = []
    kata_kunci_lower = kata_kunci.lower()
    
    # Mencoba seluruh pergeseran kunci 0 hingga 25
    for k in range(26):
        pesan_dekripsi = mesin_dekripsi(sandi, k)
        if pesan_dekripsi.lower().find(kata_kunci_lower) != -1:
            hasil_retas.append((k, pesan_dekripsi))
            
    return hasil_retas

# --- Main Program Soal 3 ---
if __name__ == "__main__":
    pesan_sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
    target_kunci = input("Masukkan kata kunci target: ")
    
    hasil = retas_sandi(pesan_sandi, target_kunci)
    print(f"Output Deskripsi: {hasil}")