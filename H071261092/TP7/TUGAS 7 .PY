import os
import random
import datetime

LOKASI_KODE = os.path.dirname(os.path.abspath(__file__))
PATH_INVOICES = os.path.join(LOKASI_KODE, "invoices")
PATH_HISTORY = os.path.join(LOKASI_KODE, "trx_history.txt")

if not os.path.exists(PATH_INVOICES):
    os.makedirs(PATH_INVOICES)

print("----------------------------------------")
print("             SELAMAT DATANG")
print("----------------------------------------")

while True:
    nama_kasir = input("Masukkan nama kasir     : ").strip()
    if nama_kasir:
        break
    print("[Peringatan] Nama kasir tidak boleh kosong!")

inisial = "".join([kata[0].upper() for kata in nama_kasir.split() if kata])
if len(inisial) < 3 and len(nama_kasir) >= 3:
    inisial = nama_kasir.replace(" ", "")[:3].upper() 

while True:
    print("----------------------------------------")
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print("----------------------------------------")
    pilihan = input("Masukkan opsi pilihan   : ").strip()
    
    if pilihan == "1":
        daftar_produk = []
        total_nominal = 0
        
        while True:
            print("----------------------------------------")
            while True:
                nama_produk = input("Masukkan nama produk    : ").strip()
                if nama_produk:
                    break
                print("[Peringatan] Nama produk tidak boleh kosong!")
            
            while True:
                try:
                    harga_produk = int(input("Masukkan harga produk   : "))
                    if harga_produk >= 0:
                        break
                    print("[Peringatan] Harga produk tidak boleh minus!")
                except ValueError:
                    print("[Peringatan] Harga harus berupa angka saja!")
            
            while True:
                try:
                    jumlah_produk = int(input("Masukkan jumlah produk  : "))
                    if jumlah_produk > 0:
                        break
                    print("[Peringatan] Jumlah produk harus lebih dari 0!")
                except ValueError:
                    print("[Peringatan] Jumlah harus berupa angka saja!")
            
            subtotal = harga_produk * jumlah_produk
            total_nominal += subtotal
            
            daftar_produk.append({
                'nama': nama_produk,
                'harga': harga_produk,
                'jumlah': jumlah_produk,
                'subtotal': subtotal
            })
            
            print("----------------------------------------")
            tambah = input("Tambah produk? (y/t)    : ").strip().lower()
            if tambah != "y":
                break
            print("----------------------------------------")
                
        waktu_sekarang = datetime.datetime.now()
        tahun = waktu_sekarang.strftime("%y")
        bulan = waktu_sekarang.strftime("%m")
        tanggal = waktu_sekarang.strftime("%d")
        jam_menit = waktu_sekarang.strftime("%H%M")
        angka_acak = str(random.randint(100, 999))
        
        id_transaksi = f"{inisial}{tahun}{bulan}{tanggal}{jam_menit}{angka_acak}"
        
        nama_file_invoice = os.path.join(PATH_INVOICES, f"{id_transaksi}.txt")
        waktu_str = waktu_sekarang.strftime("%d/%m/%y %H:%M")
        
        isi_invoice = "---------------------------------------------------\n"
        isi_invoice += f"                    TOKO {nama_kasir.upper()}\n"
        isi_invoice += "---------------------------------------------------\n"
        isi_invoice += f"Nama kasir       : {nama_kasir}\n"
        isi_invoice += f"Waktu transaksi  : {waktu_str}\n"
        isi_invoice += "---------------------------------------------------\n"
        isi_invoice += "                    Daftar Produk                  \n"
        isi_invoice += "---------------------------------------------------\n"
        isi_invoice += f"| {'Nama':<14} | {'Harga':<9} | {'Jumlah':<6} | {'Total':<11} |\n"
        isi_invoice += "---------------------------------------------------\n"
        
        for p in daftar_produk:
            nama_tampil = p['nama']
            if len(nama_tampil) > 14:
                nama_tampil = nama_tampil[:11] + "..."
            
            str_harga = f"Rp{p['harga']}"
            str_subtotal = f"Rp{p['subtotal']}"
            isi_invoice += f"| {nama_tampil:<14} | {str_harga:<9} | {p['jumlah']:^6} | {str_subtotal:<11} |\n"
            
        isi_invoice += "---------------------------------------------------\n"
        str_total = f"Rp{total_nominal}"
        isi_invoice += f"| TOTAL          |          |        | {str_total:<11} |\n"
        isi_invoice += "---------------------------------------------------\n"
        isi_invoice += "           TERIMA KASIH TELAH BERBELANJA           \n"
        isi_invoice += "--------------------------------------------------"
        
        try:
            with open(nama_file_invoice, 'w') as file_inv:
                file_inv.write(isi_invoice)
            
            print("----------------------------------------")
            print("TRANSAKSI BERHASIL")
            
            file_baru = not os.path.exists(PATH_HISTORY)
            
            with open(PATH_HISTORY, 'a') as file_his:
                if file_baru:
                    file_his.write("------------------------------------------------------------------\n")
                    file_his.write("|                        RIWAYAT TRANSAKSI                       |\n")
                    file_his.write("------------------------------------------------------------------\n")
                    file_his.write("|     Waktu      |     ID Transaksi     |    Nominal Transaksi   |\n")
                    file_his.write("------------------------------------------------------------------\n")
                
                str_nominal = f"Rp{total_nominal}"
                file_his.write(f"| {waktu_str:<14} | {id_transaksi:<20} | {str_nominal:>22} |\n")
                file_his.write("------------------------------------------------------------------\n")
                
        except IOError:
            print("Error: Gagal memproses file transaksi.")
            
    elif pilihan == "2":
        print("----------------------------------------")
        id_cari = input("Masukkan ID Transaksi saja: ").strip()
        nama_file_target = os.path.join(PATH_INVOICES, f"{id_cari}.txt")
        
        try:
            with open(nama_file_target, 'r') as file_inv:
                print("\n" + file_inv.read())
        except IOError:
            print(f"\n[Error] Invoice dengan ID '{id_cari}' tidak ditemukan.")
            
    elif pilihan == "3":
        print("----------------------------------------")
        print("SAMPAI JUMPA")
        print("----------------------------------------")
        break
    else:
        print("[Peringatan] Opsi tidak valid! Silakan pilih 1, 2, atau 3.")