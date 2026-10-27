import os              # mengelola folder dan file
import random          # menghasilkan angka acak untuk ID transaksi
from datetime import datetime  # mengambil dan mengatur tanggal serta waktu

# ==========================================
# KONSTANTA
# ==========================================

FOLDER_INVOICE = "invoices"     
FILE_RIWAYAT = "trx_history.txt"

# True untuk menguji contoh Tuprak.
# False untuk menggunakan tanggal dan waktu sebenarnya.
MODE_CONTOH = True  

ID_CONTOH = "KLS2308291250123"
WAKTU_CONTOH = datetime(2023, 8, 29, 12, 50, 10)

os.makedirs(FOLDER_INVOICE, exist_ok=True)  # membuat folder invoice


# ==========================================
# MEMBUAT ID TRANSAKSI
# ==========================================

def buat_id_transaksi(nama_kasir):
    waktu = datetime.now()
    inisial = "".join(
        kata[0] for kata in nama_kasir.strip().split()
    ).upper()

    # Menggunakan ID contoh hanya jika belum pernah dipakai.
    if MODE_CONTOH:
        id_contoh = os.path.join(               # menggabungkan bagian jalur jalur file
            FOLDER_INVOICE, ID_CONTOH + ".txt"
        )

        if inisial == "KLS" and not os.path.exists(id_contoh):  # memeriksa apakah jalur file atau folder ada
            return ID_CONTOH, WAKTU_CONTOH

    # ID otomatis untuk transaksi berikutnya.
    while True:
        id_transaksi = (
            f"{inisial}"
            f"{waktu.strftime('%y%m%d%H%M')}"
            f"{random.randint(100, 999)}"
        )

        nama_file = os.path.join(
            FOLDER_INVOICE, id_transaksi + ".txt"
        )

        if not os.path.exists(nama_file):   # memeriksa apa file tersebut ada
            return id_transaksi, waktu


# ==========================================
# SOAL 1: MEMBUAT INVOICE
# ==========================================

def buat_invoice():
    print("\n" + "=" * 50)
    print("                 TRANSAKSI KASIR")
    print("=" * 50)

    nama_kasir = input("Nama kasir: ").strip()

    if not nama_kasir:
        print("Error: Nama kasir tidak boleh kosong.")
        return

    daftar_produk = []
    total_belanja = 0

    while True:
        print("\n--- Input Produk ---")

        nama_produk = input("Nama produk: ").strip()

        if not nama_produk:
            print("Error: Nama produk tidak boleh kosong.")
            continue

        try:
            harga = int(input("Harga produk: Rp"))
            jumlah = int(input("Jumlah produk: "))

            if harga < 0:
                print("Error: Harga tidak boleh negatif.")
                continue

            if jumlah <= 0:
                print("Error: Jumlah harus lebih dari 0.")
                continue

        except ValueError:
            print("Error: Harga dan jumlah harus berupa angka bulat.")
            continue

        subtotal = harga * jumlah

        produk = {
            "nama": nama_produk,
            "harga": harga,
            "jumlah": jumlah,
            "subtotal": subtotal
        }

        daftar_produk.append(produk)
        total_belanja += subtotal

        print(f"Subtotal: Rp. {subtotal}")

        while True:
            tambah = input(
                "Tambah produk lagi? (y/n): "
            ).strip().lower()

            if tambah in ("y", "n"):
                break

            print("Input salah. Masukkan y atau n.")

        if tambah == "n":
            break

    if not daftar_produk:
        print("Transaksi dibatalkan: belum ada produk.")
        return

    id_transaksi, waktu = buat_id_transaksi(nama_kasir)

    garis = "=" * 68
    pemisah = "-" * 68

    isi_invoice = [
        garis,
        "                         INVOICE KASIR",
        garis,
        f"ID Transaksi : {id_transaksi}",
        f"Waktu        : {waktu.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Nama Kasir   : {nama_kasir}",
        pemisah,
        f"{'Nama Produk':<22}{'Harga':>12}{'Jumlah':>10}{'Subtotal':>18}",
        pemisah
    ]

    for produk in daftar_produk:
        isi_invoice.append(
            f"{produk['nama'][:22]:<22}"
            f"{produk['harga']:>12}"
            f"{produk['jumlah']:>10}"
            f"{produk['subtotal']:>18}"
        )

    isi_invoice.extend([
        pemisah,
        f"{'TOTAL BELANJA':<44}Rp. {total_belanja:>15}",
        garis,
        "                       Terima kasih!",
        garis
    ])

    teks_invoice = "\n".join(isi_invoice) + "\n"

    nama_file = os.path.join(
        FOLDER_INVOICE, id_transaksi + ".txt"
    )

    try:
        # Mode x mencegah file invoice lama tertimpa.
        with open(nama_file, "x", encoding="utf-8") as file:
            file.write(teks_invoice)

        simpan_riwayat(waktu, id_transaksi, total_belanja)

        print("\nTransaksi berhasil!")
        print(f"Invoice disimpan di: {nama_file}")
        print("\n" + teks_invoice)

    except OSError as error:
        print(f"Error saat menyimpan invoice: {error}")


# ==========================================
# SOAL 3: MENYIMPAN RIWAYAT TRANSAKSI
# ==========================================

def simpan_riwayat(waktu, id_transaksi, total):
    lebar = 72
    garis = "=" * lebar

    header = (
        f"| {'Waktu':<19} | "
        f"{'ID Transaksi':<17} | "
        f"{'Nominal Transaksi':<22} |\n"
    )

    baris = (
        f"| {waktu.strftime('%Y-%m-%d %H:%M:%S'):<19} | "
        f"{id_transaksi:<17} | "
        f"{('Rp. ' + str(total)):<22} |\n"
    )

    try:
        file_baru = (
            not os.path.exists(FILE_RIWAYAT)
            or os.path.getsize(FILE_RIWAYAT) == 0
        )

        with open(FILE_RIWAYAT, "a", encoding="utf-8") as file:
            if file_baru:
                file.write(garis + "\n")
                file.write(header)
                file.write(garis + "\n")

            file.write(baris)
            file.write(garis + "\n")

    except OSError as error:
        print(f"Error saat menyimpan riwayat: {error}")


# ==========================================
# SOAL 2: MENCARI DAN MENAMPILKAN INVOICE
# ==========================================

def cari_invoice():
    print("\n" + "=" * 50)
    print("                  CARI INVOICE")
    print("=" * 50)

    id_transaksi = input(
        "Masukkan ID transaksi: "
    ).strip()

    if not id_transaksi:
        print("Error: ID transaksi tidak boleh kosong.")
        return

    # Mencegah input path selain ID transaksi.
    if (
        not id_transaksi.isalnum()
        or not id_transaksi.isascii()
    ):
        print("Error: ID transaksi tidak valid.")
        return

    nama_file = os.path.join(
        FOLDER_INVOICE, id_transaksi + ".txt"
    )

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            isi_invoice = file.read()

        print("\nInvoice ditemukan!\n")
        print(isi_invoice)

    except FileNotFoundError:
        print("Invoice tidak ditemukan.")

    except OSError as error:
        print(f"Error saat membaca invoice: {error}")


# ==========================================
# MENAMPILKAN RIWAYAT TRANSAKSI
# ==========================================

def tampilkan_riwayat():
    print("\n" + "=" * 72)
    print("                      RIWAYAT TRANSAKSI")
    print("=" * 72)

    try:
        with open(FILE_RIWAYAT, "r", encoding="utf-8") as file:
            isi_riwayat = file.read()

        if isi_riwayat.strip():
            print(isi_riwayat)
        else:
            print("Belum ada riwayat transaksi.")

    except FileNotFoundError:
        print("Belum ada riwayat transaksi.")

    except OSError as error:
        print(f"Error saat membaca riwayat: {error}")


# ==========================================
# MENU UTAMA
# ==========================================

def menu_utama():
    while True:
        print("\n" + "=" * 50)
        print("                  APLIKASI KASIR")
        print("=" * 50)
        print("1. Membuat Invoice")
        print("2. Mencari Invoice")
        print("3. Riwayat Transaksi")
        print("4. Keluar")
        print("=" * 50)

        try:
            pilihan = input("Pilih menu (1-4): ").strip()

            if pilihan == "1":
                buat_invoice()

            elif pilihan == "2":
                cari_invoice()

            elif pilihan == "3":
                tampilkan_riwayat()

            elif pilihan == "4":
                print("Terima kasih telah menggunakan aplikasi kasir.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih 1-4.")

        except (EOFError, KeyboardInterrupt):
            print("\nProgram dihentikan.")
            break


if __name__ == "__main__":
    menu_utama()
