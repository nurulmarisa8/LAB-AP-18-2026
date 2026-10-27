from datetime import datetime
import os
import random

# Menentukan folder penyimpanan
folder_saat_ini = os.path.dirname(os.path.abspath(__file__))
folder_invoices = os.path.join(folder_saat_ini, "invoices")
file_history = os.path.join(folder_saat_ini, "trx_history.txt")

# Membuat folder 'invoices' 
os.makedirs(folder_invoices, exist_ok=True)

def membuat_invoices(kasir, data_produk):
  # Mengambil waktu saat ini untuk format ID transaksi dan isi file
  waktu_sekarang = datetime.now().strftime("%Y%m%d%H%M%S")
  id_nama = kasir[:3].upper()
  id_tahun = waktu_sekarang[2:4]
  id_bulan = waktu_sekarang[4:6]
  id_tanggal = waktu_sekarang[6:8]
  id_jam_menit = waktu_sekarang[8:12]
  angka_random = random.randint(100, 999)

  total_keseluruhan = 0

  # Menyusun ID Transaksi dan nama file
  id_transaksi = (
      f"{id_nama}{id_tahun}{id_bulan}{id_tanggal}{id_jam_menit}{angka_random}"
  )
  nama_file = f"{id_transaksi}.txt"
  file_dalam_folder = os.path.join(folder_invoices, nama_file)

  # 1. Menulis file invoice 
  try:
    with open(file_dalam_folder, "w", encoding="utf-8") as o:
      o.write("=" * 40 + "\n")
      o.write("             STRUK BELANJA              \n")
      o.write("=" * 40 + "\n")
      o.write(f"ID Transaksi : {id_transaksi}\n")
      o.write(
          f"Waktu        :"
          f" {id_tanggal}/{id_bulan}/{id_tahun} {waktu_sekarang[8:10]}:{waktu_sekarang[10:12]}\n"
      )
      o.write(f"Kasir        : {kasir}\n")
      o.write("-" * 40 + "\n")

      # Perulangan untuk menulis setiap produk ke dalam file menggunakan o.write()
      for item in data_produk:
        subtotal = item["Harga"] * item["Jumlah"]
        o.write(f"{item['Nama']} ({item['Jumlah']}x) @ Rp{item['Harga']:,.0f}\n")
        o.write(f"  Subtotal   : Rp{subtotal:,.0f}\n")
        total_keseluruhan += subtotal

      o.write("-" * 40 + "\n")
      o.write(f"TOTAL PEMBAYARAN : Rp{total_keseluruhan:,.0f}\n")
      o.write("=" * 40 + "\n")

    print("=" * 54)
    print("TRANSAKSI BERHASIL".center(54))
    print("=" * 54)
  except IOError:
    print("Error: Gagal menulis file invoice.")

  # 2. Mencatat ke file riwayat 
  try:
    with open(file_history, "a", encoding="utf-8") as isi:
      isi.write(
          f"Waktu: {id_tanggal}/{id_bulan}/{id_tahun}"
          f" {waktu_sekarang[8:10]}:{waktu_sekarang[10:12]} | ID:"
          f" {id_transaksi} | Total: Rp{total_keseluruhan:,.0f}\n"
      )
  except IOError:
    print("Error: Gagal memperbarui file riwayat.")


# --- PROGRAM UTAMA ---
print("=" * 54)
print("SELAMAT DATANG".center(54))
print("=" * 54)
nama_kasir = input("Masukkan nama kasir : ")

while True:
  print("=" * 54)
  print("Pilih opsi:")
  print("1. Transaksi baru")
  print("2. Cari transaksi")
  print("3. Keluar")
  print("=" * 54)
  pilih_opsi = input("Masukkan opsi pilihan : ")
  print("=" * 54)

  if pilih_opsi == "1":
    data_list = []
    while True:
      try:
        nama_produk = input("Masukkan nama produk : ")
        harga_produk = int(input("Masukkan harga produk : "))
        jumlah_produk = int(input("Masukkan jumlah produk : "))
        print("=" * 54)

        # Menyimpan data produk ke dalam dictionary lalu dimasukkan ke list
        data = {
            "Nama": nama_produk,
            "Harga": harga_produk,
            "Jumlah": jumlah_produk,
        }
        data_list.append(data)

        Tambah = True
        Keluar = True
        while Tambah == True:
          tambah_produk = input("Tambah produk? (y/t) : ")
          print("=" * 54)
          if tambah_produk == "y":
            Tambah = False
          elif tambah_produk == "t":
            Keluar = False
            break
          else:
            print("Input yang anda masukkan tidak valid")
            continue

        if Keluar == False:
          membuat_invoices(nama_kasir, data_list)
          break
      except ValueError:
        print("Harga atau jumlah yang anda masukkan tidak valid")
        continue

  elif pilih_opsi == "2":
    id_transaksi = input("Masukkan ID transaksi : ")
    print("=" * 54)
    lokasi_file_folder = os.path.join(folder_invoices, id_transaksi + ".txt")

    # Membaca file menggunakan mode "r" (Read) dan metode read()
    try:
      if os.path.isfile(lokasi_file_folder):
        with open(lokasi_file_folder, "r", encoding="utf-8") as ada:
          isi = ada.read()
          print("=== ISI FILE ===")
          print(isi)
      else:
        print(f"File '{id_transaksi}' tidak ditemukan.")
    except ValueError:
      print("Error: Gagal membaca file.")

  elif pilih_opsi == "3":
    print("Terima kasih!")
    break
  else:
    print("Opsi yang anda pilih tidak valid!")