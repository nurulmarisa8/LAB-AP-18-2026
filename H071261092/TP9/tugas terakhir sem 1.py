class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)
        return skor

    def status_performa(self):
        if self.hitung_skor_akhir() >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        skor_akhir = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"{no:<3} | {self.nama:<10} | {self.id_pemain:<12} | {self.role:<10} | {skor_akhir:<10.2f} | {status}")

def input_nilai_valid(teks_prompt):
    while True:
        try:
            nilai = int(input(teks_prompt))
            if nilai < 0:
                print("   -> Error: Nilai tidak boleh negatif. Silakan ketik ulang!")
            else:
                return nilai
        except ValueError:
            print("   -> Error: Input harus berupa angka bulat, bukan huruf atau teks!")

def jalankan_program():
    print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
    
    while True:
        try:
            jumlah_pemain = int(input("Masukkan jumlah pemain: "))
            if jumlah_pemain <= 0:
                print("   -> Error: Jumlah pemain tidak boleh nol atau negatif.")
            else:
                break
        except ValueError:
            print("   -> Error: Masukkan angka bulat.")
    
    daftar_pemain = []
    
    for i in range(1, jumlah_pemain + 1):
        print(f"\n--- Data Pemain ke-{i} ---")
        nama = input("Nama: ")
        id_pemain = input("ID Pemain: ")
        role = input("Role: ")
        
        nilai_kill = input_nilai_valid("Nilai Kill: ")
        nilai_assist = input_nilai_valid("Nilai Assist: ")
        nilai_objective = input_nilai_valid("Nilai Objective: ")
        
        pemain_baru = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective)
        daftar_pemain.append(pemain_baru)
        
    print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
    print(f"{'No':<3} | {'Nama':<10} | {'ID Pemain':<12} | {'Role':<10} | {'Skor Akhir':<10} | {'Status'}")
    print("-" * 75)
    
    for i, pemain in enumerate(daftar_pemain, start=1):
        pemain.tampilkan_data(i)

if __name__ == "__main__":
    jalankan_program()