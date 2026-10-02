def hitung_mundur(angka):
    if angka < 0:
        return
    print(angka)
    if angka == 0:
        print("Luncurkan!")
        return
    hitung_mundur(angka - 1)

def main():
    while True:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))
        if angka_awal < 0:
            print("Input tidak valid, angka tidak boleh negatif.")
        else:
            hitung_mundur(angka_awal)
            break

if __name__ == "__main__":
    main()