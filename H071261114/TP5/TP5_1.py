ALFABET_KECIL = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    teks_bersih = ""
    for char in teks:
        char_lower = char.lower()
        if char_lower in ALFABET_KECIL:
            teks_bersih += char_lower
    return teks_bersih

def cek_palinrome(teks):
    teks_terbalik = "".join(reversed(teks))
    if teks == teks_terbalik:
        return (True, -1)
    else:
        for i in range(len(teks)):
            if teks[i] != teks_terbalik[i]:
                return (False, i)

def inti_palinrome(teks):
    teks_b = bersihkan_teks(teks)
    n = len(teks_b)
    
    max_len = 0
    best_sub = ""
    best_idx = 0
    
    # Mencari substring palindrom terpanjang (prioritas paling kiri)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks_b[i:j]
            is_palin, _ = cek_palinrome(sub)
            if is_palin:
                length = len(sub)
                if length > max_len:
                    max_len = length
                    best_sub = sub
                    best_idx = i
                    
    return {
        "teks": best_sub,
        "panjang": max_len,
        "indeks_awal": best_idx
    }

# --- Main Program Soal 1 ---
if __name__ == "__main__":
    input_teks = input("Masukkan teks prasasti: ")
    teks_b = bersihkan_teks(input_teks)
    hasil = inti_palinrome(input_teks)
    
    print(f"Teks Bersih: {teks_b}")
    print(f"Output Terharap: {hasil}")