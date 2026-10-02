# Konversi Suhu (try-except & raise)

def konversi_suhu(nilai, skala_asal, skala_tujuan):
    asal = skala_asal.upper()
    tujuan = skala_tujuan.upper()

    skala_valid = ['C', 'F', 'K']
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali")

    # Konversi asal ke Celsius
    if asal == 'C':
        celsius = nilai
    elif asal == 'F':
        celsius = (nilai - 32) * 5/9
    elif asal == 'K':
        celsius = (nilai - 273.15)

    # Konversi Celsius ke tujuan
    if tujuan == 'C':
        hasil = celsius
    elif tujuan == 'F':
        hasil = (celsius * 9/5) + 32
    elif tujuan == 'K':
        hasil = celsius + 273.15

    return hasil

def main_cuaca():
    print("=== Konversi Suhu ===")
    while True:
        inp_suhu = input("Masukkan suhu (atau 'Selesai' untuk keluar): ")
        if inp_suhu.lower() == 'Selesai':
            break

        skala_asal = input("Skala asal (C/F/K): ")
        skala_tujuan = input ("Skala tujuan (C/F/K): ")

        try:
            suhu = float(inp_suhu)
            hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)

            fmt_suhu = f"{int(suhu)}.0" if suhu.is_integer() else f"{suhu}"
            fmt_hasil = f"{int(hasil)}.0" if hasil.is_integer() else f"{hasil:.1}"

            print(f"Hasil: {fmt_suhu} {skala_asal.upper()} = {fmt_hasil} {skala_tujuan.upper()}")
        except ValueError as e:
            if "Skala suhu tidak dikenali" in str(e):
                print(e)
            else:
                print("Error: Input suhu harus berupa angka")

if __name__ == "__main__":
    main_cuaca()


