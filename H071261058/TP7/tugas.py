from datetime import datetime
import random
import os

folder_saat_ini = os.path.dirname(os.path.abspath(__file__))
folder_invoices = os.path.join(folder_saat_ini, "invoices")
file_history = os.path.join(folder_saat_ini, "trx_history.txt")
os.makedirs(folder_invoices, exist_ok=True)   
garis = "=" * 54

def membuat_invoices(kasir, data_produk):
    waktu = datetime.now()
    kode_waktu = waktu.strftime("%y%m%d%H%M")        
    waktu_tampil = waktu.strftime("%d/%m/%y %H:%M")  
    angka_random = random.randint(100, 999)
    id_transaksi = kasir[:3].upper() + kode_waktu + str(angka_random)
    lokasi_file = os.path.join(folder_invoices, id_transaksi + ".txt")

    border = "=" * 79
    judul_kolom = "|" + "Nama".center(38) + "|" + "Harga".center(14) + "|" + "Jumlah".center(8) + "|" + "Total".center(14) + "|"

    total_keseluruhan = 0
    with open(lokasi_file, "w") as file:
        file.write(f"TOKO {kasir.capitalize()}".center(100) + "\n")
        file.write("=" * 100 + "\n")
        file.write("Nama kasir         : " + kasir + "\n")
        file.write("Waktu transaksi    : " + waktu_tampil + "\n")
        file.write("=" * 100 + "\n")
        file.write("\n")
        file.write("Daftar Produk".center(100) + "\n")
        file.write("\n")
        file.write(border.center(100) + "\n")
        file.write(judul_kolom.center(100) + "\n")
        file.write(border.center(100) + "\n")

        for produk in data_produk:
            nama = produk["Nama"]
            harga = produk["Harga"]
            jumlah = produk["Jumlah"]
            total_item = harga * jumlah
            total_keseluruhan += total_item
            baris = "| " + nama.ljust(37) + "|" + f"Rp{harga}".rjust(13) + " |" + str(jumlah).center(8) + "|" + f"Rp{total_item}".rjust(13) + " |"
            file.write(baris.center(100) + "\n")

        baris_total = "|" + "TOTAL".center(38) + "|".rjust(25) + f"Rp{total_keseluruhan}".rjust(13) + " |"
        file.write(border.center(100) + "\n")
        file.write(baris_total.center(100) + "\n")
        file.write(border.center(100) + "\n")
        file.write("\n")
        file.write("=" * 100 + "\n")
        file.write("TERIMAKASIH TELAH BELANJA".center(100) + "\n")
        file.write("=" * 100 + "\n")

    with open(file_history, "a") as file:
        file.write("\n| " + waktu_tampil.ljust(28) + "| " + id_transaksi.ljust(29) + "|" + f"Rp{total_keseluruhan}".rjust(26) + " |")
        file.write("\n" + "=" * 90)

    print(garis)
    print("TRANSAKSI BERHASIL".center(54))


print(garis)
print("SELAMAT DATANG".center(54))
print(garis)
nama_kasir = input("Masukkan nama kasir \t : ")

while True:
    print(garis)
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. keluar")
    print(garis)
    pilih_opsi = input("Masukkan opsi pilihan \t : ")
    print(garis)

    if pilih_opsi == "1":
        data_list = []
        while True:
            try:
                nama_produk = input("Masukkan nama produk \t : ")
                harga_produk = int(input("Masukkan harga produk \t : "))
                jumlah_produk = int(input("Masukkan jumlah produk \t : "))
            except ValueError:
                print("Harga yang anda masukkan tidak valid")
                continue

            data = {
                "Nama": nama_produk,
                "Harga": harga_produk,
                "Jumlah": jumlah_produk,
            }
            data_list.append(data)

            while True:
                print(garis)
                tambah_produk = input("Tambah produk? (y/t) \t : ")
                print(garis)
                if tambah_produk == "y" or tambah_produk == "t":
                    break
                print("Input yang anda masukkan tidak valid")

            if tambah_produk == "t":
                membuat_invoices(nama_kasir, data_list)
                break


    elif pilih_opsi == "2":
        id_transaksi = input("Masukkan ID transaksi \t : ")
        lokasi_file_folder = os.path.join(folder_invoices, id_transaksi + ".txt")
        if os.path.isfile(lokasi_file_folder):
            with open(lokasi_file_folder, "r") as file:
                isi = file.read()
            print("=== ISI FILE ===")
            print(isi)
        else:
            print(f"File '{id_transaksi}' tidak ditemukan.")


    elif pilih_opsi == "3":
        print("Terimas kasih!")
        break

    else:
        print("Opsi yang anda pilih tidak valid!")