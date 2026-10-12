alfabet = "abcdefghijklmnopqrstuvwxyz" 

def cek_kata(teks, kata): 
    hasil = [] 
    if kata == "": 
        return hasil 
    teks_kecil = teks.lower() 
    kata_kecil = kata.lower() 
    start = 0 
    while True: 
        start = teks_kecil.find(kata_kecil, start) 
        if start == -1: 
            break 
        hasil.append(start) 
        start += len(kata_kecil) 
    return hasil 

def cek_batas_kata(teks, i, panjang): 
    teks_kecil = teks.lower()
    if panjang > 0: 
        if i > 0 and teks_kecil[i-1] in alfabet: 
            return False 
        if i + panjang < len(teks) and teks_kecil[i + panjang] in alfabet: 
            return False 
    return True 

def sensor_kata(teks, kata, simbol): 
    panjang = len(kata) 
    indeks = cek_kata(teks, kata) 
    hasil = "" 
    i = 0 
    n = len(teks) 
    jumlah_tersensor = 0 
    list_indeks_awal = [] 
    
    while i < n: 
        if i in indeks and cek_batas_kata(teks, i, panjang): 
            hasil += simbol * panjang 
            list_indeks_awal.append(i) 
            jumlah_tersensor += 1 
            i += panjang 
        else: 
            hasil += teks[i] 
            i += 1 
    return hasil, jumlah_tersensor, list_indeks_awal

while True: 
    teks = input("Masukkan Teks: ") 
    if teks == "": 
            break 
    kata = input("Masukkan kata target: ") 
    simbol = input("Masukkan simbol: ") 
        
    teks_tersensor, jumlah_tersensor, list_indeks_awal = sensor_kata(teks, kata, simbol) 
    
    print("Hasil Teks: ", teks_tersensor) 
    print("Jumlah: ", jumlah_tersensor, "| Indeks: ", list_indeks_awal)