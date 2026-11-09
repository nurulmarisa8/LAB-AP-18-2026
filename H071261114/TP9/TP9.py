class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        print(f"| {no:<3} | {self.nama:<10} | {self.id_pemain:<11} | {self.role:<9} | "
            f"{self.hitung_skor_akhir():<10.2f} | {self.status_performa():<14} |")


def input_angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input harus berupa angka, coba lagi.")


def input_jumlah(pesan):
    while True:
        try:
            jumlah = int(input(pesan))
            if jumlah > 0:
                return jumlah
            print("Jumlah pemain harus lebih dari 0.")
        except ValueError:
            print("Input harus berupa bilangan bulat, coba lagi.")


def main():
    print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===\n")
    jumlah = input_jumlah("Masukkan jumlah pemain: ")

    daftar_pemain = []
    for i in range(1, jumlah + 1):
        print(f"\n-- Data Pemain ke-{i} --")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        nilai_kill = input_angka("Nilai Kill: ")
        nilai_assist = input_angka("Nilai Assist: ")
        nilai_objective = input_angka("Nilai Objective: ")
        daftar_pemain.append(
            Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
        )

    garis = "=" * 79
    print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
    print(garis)
    print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<9} | "
        f"{'Skor Akhir':<10} | {'Status':<14} |")
    print(garis)
    for no, pemain in enumerate(daftar_pemain, start=1):
        pemain.tampilkan_data(no)
    print(garis)


if __name__ == "__main__":
    main()