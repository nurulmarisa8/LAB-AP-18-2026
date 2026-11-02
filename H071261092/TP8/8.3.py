import re

data_awal = []

def bersihkan_dan_validasi():
    print("=== Pembersihan Data Nomor Telepon ===")
    print()
    
    try:
        jumlah_data = int(input("Masukkan jumlah data: "))
    except ValueError:
        print("Harap masukkan angka yang valid!")
        return

    for i in range(1, jumlah_data + 1):
        nomor = input(f"Nomor ke-{i}: ")
        data_awal.append(nomor)
        
    print("\n--- Hasil Pembersihan ---\n")
    
    nomor_valid_count = 0
    
    for idx, nomor_asal in enumerate(data_awal, 1):
        nomor_bersih = re.sub(r'[\s-]', '', nomor_asal)
        
        is_valid = bool(re.match(r'^\d{10,13}$', nomor_bersih))
        
        if is_valid:
            status = "Valid"
            nomor_valid_count += 1
        else:
            status = "Tidak valid"
            
        print(f"Data {idx}:")
        print(f"Sebelum : {nomor_asal}")
        print(f"Sesudah : {nomor_bersih}")
        print(f"Status  : {status}")
        print()
        
    print(f"Jumlah nomor valid: {nomor_valid_count}")

if __name__ == "__main__":
    bersihkan_dan_validasi()
