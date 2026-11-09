class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        if nama.strip() == "":
            raise ValueError("Nama pemain tidak boleh kosong.")
        if id_pemain.strip() == "":
            raise ValueError("ID pemain tidak boleh kosong.")
        if role.strip() == "":
            raise ValueError("Role pemain tidak boleh kosong.")
        if nilai_kill < 0 or nilai_assist < 0 or nilai_objective < 0:
            raise ValueError("Nilai Kill, Assist, dan Objective tidak boleh negatif.")

        self.nama = nama.strip()
        self.id_pemain = id_pemain.strip()
        self.role = role.strip()
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, nomor):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {nomor:<3} | {self.nama:<10} | {self.id_pemain:<10} | "
              f"{self.role:<10} | {skor:<10.2f} | {status:<14} |")

def input_angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("  Input harus berupa angka, coba lagi.")
            
def input_jumlah(pesan):
    while True:
        try:
            jumlah = int(input(pesan))
            if jumlah <= 0:
                raise ValueError("Jumlah harus lebih dari 0.")
            return jumlah
        except ValueError:
            print("  Input harus berupa bilangan bulat lebih dari 0, coba lagi.")

def main():
    daftar_pemain = []

    print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
    print()
    jumlah = input_jumlah("Masukkan jumlah pemain: ")

    for i in range(1, jumlah + 1):
        print()
        print(f"-- Data Pemain ke-{i} --")

        while True:
            nama = input("Nama: ")
            id_pemain = input("ID Pemain: ")
            role = input("Role: ")
            nilai_kill = input_angka("Nilai Kill: ")
            nilai_assist = input_angka("Nilai Assist: ")
            nilai_objective = input_angka("Nilai Objective: ")

            try:
                pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
                daftar_pemain.append(pemain)
                break  
            except ValueError as e:
                print(f"  Data tidak valid: {e}")
                print("  Silakan masukkan ulang data pemain ini.\n")

    garis = "=" * 76
    print()
    print("=== REKAPITULASI PERFORMA PEMAIN ===")
    print(garis)
    print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<10} | "
          f"{'Role':<10} | {'Skor Akhir':<10} | {'Status':<14} |")
    print(garis)

    for nomor, pemain in enumerate(daftar_pemain, start=1):
        pemain.tampilkan_data(nomor)

    print(garis)

main()