persentase = int(input("Masukkan persentase cabai: "))

if persentase >= 0 and persentase <= 10:
    print("Level Aman")
elif persentase  >= 11 and persentase <= 40 :
    print("Level Sedang")
elif persentase  >= 41 and persentase <= 70 :
    print("Level Pedas")
elif persentase  > 70 and persentase <= 100:
    print("Level Ekstrem")
else:
    print("Input Tidak Valid")