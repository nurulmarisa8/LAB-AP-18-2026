# Class Pemain  (cetakan untuk membuat objek)
class Pemain:

    # Constructor   (dijalankan saat objek dibuat) self(mengakses atribut dan method object)
    def __init__(self, nama, id_pemain, role,
                 nilai_kill, nilai_assist, nilai_objective):

        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    # Method menghitung skor akhir (fungsi yang berada di dalam class)
    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + \
               (0.3 * self.nilai_assist) + \
               (0.4 * self.nilai_objective)

        return skor

    # Method menentukan status performa
    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    # Method menampilkan data pemain
    def tampilkan_data(self, no):
        print(f"| {no:<3} | {self.nama:<10} | "
              f"{self.id_pemain:<11} | {self.role:<9} | "
              f"{self.hitung_skor_akhir():<10.2f} | "
              f"{self.status_performa():<15} |")


# List untuk menyimpan objek pemain
daftar_pemain = []

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
print()

# Input jumlah pemain
while True:
    try:
        jumlah = int(input("Masukkan jumlah pemain: "))

        if jumlah <= 0:
            print("Jumlah pemain harus lebih dari 0!")
        else:
            break

    except ValueError:
        print("Error! Masukkan jumlah pemain berupa angka.")


# Perulangan input data pemain
for i in range(jumlah):

    print(f"\n-- Data Pemain ke-{i+1} --")

    nama = input("Nama             : ")
    id_pemain = input("ID Pemain        : ")
    role = input("Role             : ")

    # Input nilai dengan try-except
    while True:
        try:
            nilai_kill = float(input("Nilai Kill       : "))
            nilai_assist = float(input("Nilai Assist     : "))
            nilai_objective = float(input("Nilai Objective  : "))

            if nilai_kill < 0 or nilai_assist < 0 or nilai_objective < 0:
                print("Error! Nilai tidak boleh negatif.")
                continue

            break

        except ValueError:
            print("Error! Nilai harus berupa angka.")
            print("Silakan masukkan kembali nilai pemain.")

    # Membuat objek pemain
    pemain = Pemain(
        nama,
        id_pemain,
        role,
        nilai_kill,
        nilai_assist,
        nilai_objective
    )

    # Menambahkan objek ke dalam list
    daftar_pemain.append(pemain)


# Menampilkan rekapitulasi performa pemain
print("\n=== REKAPITULASI PERFORMA PEMAIN ===")

print("=" * 80)

print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<11} | "
      f"{'Role':<9} | {'Skor Akhir':<10} | {'Status':<15} |")

print("=" * 80)

# Perulangan menampilkan seluruh data pemain
for i, pemain in enumerate(daftar_pemain, start=1):
    pemain.tampilkan_data(i)

print("=" * 80)
#Class = Cetakan untuk membuat objek
#Object = Hasil dari Class
#Attribute = Data yang dimiliki objek
#Method = Fungsi yang berada di dalam class.
#Constructor = Method khusus __init__() yang dijalankan saat objek dibuat
#Self = Mengacu pada objek yang sedang digunakan