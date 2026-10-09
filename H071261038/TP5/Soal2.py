# Sensor Kata

# 1. Fungsi untuk mencari indeks kemunculan kata (tidak peka huruf besar/kecil)
def cek_kata(teks, kata):
    t, k, res, start = teks.lower(), kata.lower(), [], 0
    while True:
        idx = t.find(k, start)
        if idx == -1: break
        res.append(idx)
        start = idx + 1
    return res

# 2. Fungsi untuk memastikan kata yang ditemukan adalah kata utuh (bukan bagian kata lain)
def cek_batas_kata(teks, i, p):
    n = len(teks)
    if i > 0  and 'a' <= teks[i-1].lower() <='z': return False
    if i + p < n and 'a' <= teks[i+p].lower() <= 'z': return False
    return True

# 3. Fungsi utama penyensoran kata
def sensor_kata(teks, kata, simbol):
    list = [i for i in cek_kata(teks, kata) if cek_batas_kata(teks, i, len(kata))]
    res, i, p = "", 0, len(kata)
    while i < len(teks):
        if i in list:
            res, i = res + (simbol * p), i + p
        else:
            res, i = res + teks[i], i + 1
    return res, len(list), list

# 4. Program utama dengan validasi input
while True:
    t = input("Masukkan Teks: ")
    if any(c.isalnum() for c in t): break
    print("Teks harus ada huruf/angka!")

while True:
    k = input("Masukkan kata target: ")
    if any(k.isdigit() for k in t) : break
    print("Kata target harus huruf!")

s = input("Masukkan simbol: ")
res_t, jml, idxs = sensor_kata(t, k, s)
print(f"Hasil Teks: {res_t}\nJumlah: {jml} | Indeks: {idxs}")