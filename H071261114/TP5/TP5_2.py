ALFABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cek_kata(teks, kata):
    indeks_list = []
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    
    start = 0
    while True:
        idx = teks_lower.find(kata_lower, start)
        if idx == -1:
            break
        indeks_list.append(idx)
        start = idx + 1
    return indeks_list

def cek_batas_kata(teks, i, panjang):
    # Cek karakter sebelum kata target
    if i > 0:
        if teks[i - 1] in ALFABET:
            return False
            
    # Cek karakter sesudah kata target
    idx_sesudah = i + panjang
    if idx_sesudah < len(teks):
        if teks[idx_sesudah] in ALFABET:
            return False
            
    return True

def sensor_kata(teks, kata, simbol):
    kemunculan = cek_kata(teks, kata)
    panjang_kata = len(kata)
    
    list_indeks_awal = []
    for idx in kemunculan:
        if cek_batas_kata(teks, idx, panjang_kata):
            list_indeks_awal.append(idx)
            
    # Merakit ulang teks secara manual
    teks_tersensor = ""
    i = 0
    n = len(teks)
    
    while i < n:
        if i in list_indeks_awal:
            teks_tersensor += simbol * panjang_kata
            i += panjang_kata
        else:
            teks_tersensor += teks[i]
            i += 1
            
    return (teks_tersensor, len(list_indeks_awal), list_indeks_awal)

# --- Main Program Soal 2 ---
if __name__ == "__main__":
    teks_input = input("Masukkan Teks: ")
    kata_target = input("Masukkan kata target: ")
    simbol_input = input("Masukkan simbol: ")
    
    hasil_teks, jumlah, idx_list = sensor_kata(teks_input, kata_target, simbol_input)
    
    print(f"Hasil Teks: {hasil_teks}")
    print(f"Jumlah: {jumlah}  Indeks: {idx_list}")