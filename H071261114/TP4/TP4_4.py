def konversi_suhu(suhu, asal, tujuan):
    skala_valid = ['C', 'F', 'K']
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Error: Skala suhu tidak dikenali.")
    
    # Konversi ke Celsius terlebih dahulu sebagai basis
    if asal == 'C':
        celsius = suhu
    elif asal == 'F':
        celsius = (suhu - 32) * 5 / 9
    elif asal == 'K':
        celsius = suhu - 273.15
        
    # Konversi dari Celsius ke skala tujuan
    if tujuan == 'C':
        hasil = celsius
    elif tujuan == 'F':
        hasil = (celsius * 9 / 5) + 32
    elif tujuan == 'K':
        hasil = celsius + 273.15
        
    return hasil

print("=== Konversi Suhu ===")
while True:
    suhu_input = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if suhu_input.lower() == 'selesai':
        break
    
    suhu = float(suhu_input)
    skala_asal = input("Skala asal (C/F/K): ").strip().upper()
    skala_tujuan = input("Skala tujuan (C/F/K): ").strip().upper()
    
    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
    except ValueError as e:
        print(e)