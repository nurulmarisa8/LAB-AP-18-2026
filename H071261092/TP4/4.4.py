def konversi_suhu(suhu, asal, tujuan):
    if asal not in ['C', 'F', 'K'] or tujuan not in ['C', 'F', 'K']:
        raise ValueError("Error: Skala suhu  tidak dikenali")

    
    if asal == "C":
        c = suhu
    elif asal == "K":
        c = suhu - 273.15
    else:
        c = (suhu - 32) * 5/9

    if tujuan == "C":
        hasil = c
    elif tujuan == "F":
        hasil = (c * 9/5) + 32
    elif tujuan == "K":
        hasil = c + 273.15

    return hasil

print("=== Konversi Suhu ===")
while True:
        input_suhu = input("Masukkan suhu (ketik selesai untuk keluar): ")
        if input_suhu == "selesai":
            break

        try:
            asal = input("Masukkan skala asal (C/F/K): ").upper()
            tujuan = input("Masukkan skala tujuan (C/F/K): ").upper()
            hasil = konversi_suhu(float(input_suhu), asal, tujuan)
            print(f"Hasil: {input_suhu} {asal} = {hasil} {tujuan}")
        except ValueError as e:
            print(e)