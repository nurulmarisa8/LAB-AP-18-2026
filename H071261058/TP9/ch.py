class pemain :
    def __init__(self,nama,id_pemain,role,nilai_kill,nilai_assist,nilai_objective) :
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir (self) :
       return (self.nilai_kill * 30 + self.nilai_assist * 30 + self.nilai_objective * 40) / 100
    
    def status_performa(self) :
        if self.hitung_skor_akhir() >= 60 :
            return "Unggul"
        else :
            return "Perlu Evaluasi"
                
    def tampilkan_data(self) :
        print(f"| {i+1:<3}| {self.nama:<20}| {self.id_pemain:<17}| {self.role:<15}| {self.hitung_skor_akhir():<10.2f}| {self.status_performa():<15}|")

def input_nilai(n, nama_bagian):
    while True:
        try:
            nilai = int(input(n))
            if nilai < 0:
                print(f"Nilai {nama_bagian} tidak boleh negatif !!")
            elif nilai > 100:
                print(f"Nilai {nama_bagian} tidak boleh lebih dari 100 !!")
            else:
                return nilai
        except ValueError:
            print(f"Nilai {nama_bagian} harus berupa angka!! :) ")
            continue

def kata (keterangan,huruf) :
    while True :
        kata = input(keterangan).strip()
        if kata == "" :
            print (f"Input {huruf} tidak boleh kosong !!")
        else :
            return kata
        
print ("=== SISTEM PENILAIAN PERFORMA PEMAIN ===".center(50))
while True :
    try :
        data = input("Masukkan jumlah pemain : ")
        if data >= "1" :
            jumlah_pemain = int(data)
            break
        else :
            print ("Jumlah pemain harus lebih dari 0")
    except ValueError :
        print ("Input gak valid. Jumlah pemain harus berupa angka!!!!.")

stastistik_pemain = []
for i in range (jumlah_pemain) :
    print(f"--- Data Pemain ke-{i+1} ---")
    nama = kata("Masukkan nama pemain : ", "Nama")
    id_pemain = kata("Masukkan ID pemain : ", "ID")
    role = kata("Masukkan role pemain : ", "Role")
    nilai_kill = input_nilai("Masukkan nilai Kill : ", "Kill")
    nilai_assist = input_nilai("Masukkan nilai Assist : ", "Assist")
    nilai_objective = input_nilai("Masukkan nilai Objective : ", "Objective")

    pemainc = pemain(nama,id_pemain,role,nilai_kill,nilai_assist,nilai_objective)
    stastistik_pemain.append(pemainc)
print ()
print ("=== REKAPITULASI PERFORMA PEMAIN ===".center(93))
print("="*93)
print (f"| {'No':<3}| {'Nama Pemain':<20}| {'ID Pemain':<17}| {'Role Pemain':<15}| {'Skor Akhir':<10}| {'Status Performa':<15}|")
for i, pemain in enumerate(stastistik_pemain) : 
    pemain.tampilkan_data()
print("="*93) 