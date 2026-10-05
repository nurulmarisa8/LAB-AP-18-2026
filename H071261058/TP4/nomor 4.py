def konversi_suhu(suhu, skala_asal, skala_tujuan):
    if skala_asal not in ("C", "F", "K") or skala_tujuan not in ("C", "F", "K"):
        raise ValueError("Skala suhu tidak dikenali.")

    if skala_asal == "C":
        celsius = suhu
    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:
        celsius = suhu - 273.15

    if skala_tujuan == "C":
        return celsius
    elif skala_tujuan == "F":
        return celsius * 9 / 5 + 32
    else:
        return celsius + 273.15


print("=== Konversi Suhu ===")
while True:
    teks = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if teks == "selesai":
        break
    suhu = float(teks)
    skala_asal = input("Skala asal (C/F/K): ")
    skala_tujuan = input("Skala tujuan (C/F/K): ")

    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
    except ValueError:
        print("Error: Skala suhu tidak dikenali.")