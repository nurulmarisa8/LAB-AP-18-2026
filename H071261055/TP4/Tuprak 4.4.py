def konversi_suhu(suhu, asal, tujuan):
    skala_valid = {'C', 'F', 'K'}
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")
   
    if asal == 'C':
        celsius = suhu
    elif asal == 'F':
        celsius = (suhu - 32) * 5/9
    elif asal == 'K':
        celsius = suhu - 273.15
        
    if tujuan == 'C':
        hasil = celsius
    elif tujuan == 'F':
        hasil = (celsius * 9/5) + 32
    elif tujuan == 'K':
        hasil = celsius + 273.15
        
    return hasil

print("=== Konversi Suhu ===")
while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if input_suhu.lower() == 'selesai':
        break
    
    suhu = float(input_suhu)
    asal = input("Skala asal (C/F/K): ").upper()
    tujuan = input("Skala tujuan (C/F/K): ").upper()
    
    try:
        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
    except ValueError as error:
        print(f"Error: {error}")