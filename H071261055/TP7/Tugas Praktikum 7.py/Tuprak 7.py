import os
import random
from datetime import datetime

FOLDER_INVOICE = "invoices"
FILE_HISTORY = "trx_history.txt"
LEBAR = 50
GARIS = "=" * LEBAR
LEBAR_LABEL = 25



def tanya(label):
    
    return input(f"{label:<{LEBAR_LABEL}}: ")


def input_teks(label):

    while True:
        try:
            teks = tanya(label).strip()
            if teks == "":
                raise ValueError("Input tidak boleh kosong.")
            return teks
        except ValueError as e:
            print(f"[Error] {e}")


def input_nama_kasir(label):
    
    while True:
        try:
            nama = tanya(label).strip()
            if not any(c.isalpha() for c in nama):
                raise ValueError("Nama kasir harus berisi huruf.")
            return nama
        except ValueError as e:
            print(f"[Error] {e}")


def input_angka(label, minimal=1):
   
    while True:
        try:
            nilai = int(tanya(label))  
            if nilai < minimal:
                raise ValueError(f"Nilai minimal adalah {minimal}.")
            return nilai
        except ValueError as e:
            if "invalid literal" in str(e):
                print("[Error] Input harus berupa angka bulat (tanpa huruf, titik, atau koma).")
            else:
                print(f"[Error] {e}")


def input_ya_tidak(label):
   
    while True:
        try:
            jawab = tanya(label).strip().lower()
            if jawab not in ("y", "t"):
                raise ValueError("Jawab dengan 'y' atau 't'.")
            return jawab
        except ValueError as e:
            print(f"[Error] {e}")


# ---------- Soal 1: Membuat invoice ----------
def buat_inisial(nama):
    return "".join(kata[0] for kata in nama.split() if kata[0].isalpha()).upper()


def buat_id_transaksi(nama_kasir, waktu):
    inisial = buat_inisial(nama_kasir)
    angka_acak = random.randint(100, 999)
    return f"{inisial}{waktu.strftime('%y%m%d%H%M')}{angka_acak}"


def buat_transaksi(nama_kasir):
    daftar_belanja = []

    while True:
        nama = input_teks("Masukkan nama produk")
        harga = input_angka("Masukkan harga produk", minimal=1)
        jumlah = input_angka("Masukkan jumlah produk", minimal=1)
        daftar_belanja.append((nama, harga, jumlah))
        print(GARIS)

        lagi = input_ya_tidak("Tambah produk? (y/t)")
        print(GARIS)
        if lagi == "t":
            break

    waktu = datetime.now()
    id_trx = buat_id_transaksi(nama_kasir, waktu)
    total = sum(harga * jumlah for _, harga, jumlah in daftar_belanja)

    # Simpan invoice
    os.makedirs(FOLDER_INVOICE, exist_ok=True)
    path = os.path.join(FOLDER_INVOICE, f"{id_trx}.txt")
    with open(path, "w") as f:
        f.write(GARIS + "\n")
        f.write("INVOICE".center(LEBAR) + "\n")
        f.write(GARIS + "\n")
        f.write(f"ID Transaksi : {id_trx}\n")
        f.write(f"Waktu        : {waktu.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Kasir        : {nama_kasir}\n")
        f.write("-" * LEBAR + "\n")
        for nama, harga, jumlah in daftar_belanja:
            f.write(f"{nama}\n")
            f.write(f"  {jumlah} x Rp. {harga} = Rp. {harga * jumlah}\n")
        f.write("-" * LEBAR + "\n")
        f.write(f"TOTAL        : Rp. {total}\n")
        f.write(GARIS + "\n")
        f.write("Terima kasih sudah berbelanja!".center(LEBAR) + "\n")

    catat_riwayat(waktu, id_trx, total)

    print("TRANSAKSI BERHASIL".center(LEBAR))
    print(GARIS)


# ---------- Soal 2: Mencari invoice ----------
def cari_invoice():
    id_trx = input_teks("Masukkan ID transaksi")
    if id_trx.lower().endswith(".txt"):  
        id_trx = id_trx[:-4]
    print(GARIS)

    path = os.path.join(FOLDER_INVOICE, f"{id_trx}.txt")
    try:
        with open(path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"[Error] Invoice dengan ID '{id_trx}' tidak ditemukan.")
        print(GARIS)


# ---------- Soal 3: Riwayat transaksi ----------
def catat_riwayat(waktu, id_trx, nominal):
    garis = "=" * 64
    baru = not os.path.exists(FILE_HISTORY)
    with open(FILE_HISTORY, "a") as f:
        if baru:
            f.write(garis + "\n")
            f.write(f"| {'Waktu':<19} | {'ID Transaksi':<18} | {'Nominal Transaksi':<17} |\n")
            f.write(garis + "\n")
        f.write(
            f"| {waktu.strftime('%Y-%m-%d %H:%M:%S'):<19} | {id_trx:<18} | "
            f"{'Rp. ' + str(nominal):<17} |\n"
        )
        f.write(garis + "\n")


# ---------- Menu utama ----------
def main():
    print(GARIS)
    print("SELAMAT DATANG".center(LEBAR))
    print(GARIS)

    nama_kasir = input_nama_kasir("Masukkan nama kasir")
    print(GARIS)

    while True:
        print("Pilih opsi:")
        print("1. Transaksi baru")
        print("2. Cari transaksi")
        print("3. Keluar")
        print(GARIS)

        try:
            opsi = int(tanya("Masukkan opsi pilihan"))
        except ValueError:
            print(GARIS)
            print("[Error] Pilihan harus berupa angka 1-3.")
            print(GARIS)
            continue
        print(GARIS)

        if opsi == 1:
            buat_transaksi(nama_kasir)
        elif opsi == 2:
            cari_invoice()
        elif opsi == 3:
            print("Terima kasih sudah berbelanja!".center(LEBAR))
            print(GARIS)
            break
        else:
            print("[Error] Pilihan hanya 1, 2, atau 3.")
            print(GARIS)


if __name__ == "__main__":
    main()