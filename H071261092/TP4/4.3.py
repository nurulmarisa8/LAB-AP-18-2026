def hitung_mundur(waktu):
    if waktu <= 0:
        return
    else:
        print(waktu)
        hitung_mundur(waktu - 1)

while True:
    try:
        angka = int(input("Masukkan angka awal hitung mundur : "))
        if angka < 0:
            print("Angka tidak boleh negatif.")
            continue
        hitung_mundur(angka)
        print("luncurkan !")
        break
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")