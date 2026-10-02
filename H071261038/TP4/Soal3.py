# Hitung Mundur Roket (Fungsi Rekursif)

def hitung_mundur(n):
    print(n)
    if n == 0:
        print("Luncurkan!")
        return

    hitung_mundur(n-1)

def main_roket():
    while True:
        try:
            angka = int(input("Masukkan angka awal hitung mundur: "))
            if angka < 0:
                print("Input tidak valid, angka tidak boleh negatif")
                continue

            hitung_mundur(angka)
            break
        except ValueError:
            print("Input tidak valid, masukkan angka bulat")

if __name__=="__main__": 
     main_roket()
        

