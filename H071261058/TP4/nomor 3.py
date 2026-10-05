def hitung_mundur(n):
    print(n)
    if n > 0: 
        hitung_mundur(n - 1)
    else:
        print("Luncurkan!")
while True:
    awal = int(input("Masukkan angka awal hitung mundur: "))
    if awal < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
    else:
        break

hitung_mundur(awal)