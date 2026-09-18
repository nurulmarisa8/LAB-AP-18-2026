persen = float(input("Masukkan persentase cabai: "))
if persen >= 0 and persen <= 10:
    print("Level Aman")
elif persen >= 11 and persen <= 40:
    print("Level Sedang")
elif persen >= 41 and persen <= 70:
    print("Level Pedas")
elif persen > 70:
    print("Level Ekstrem")
else:
    print("anda salah memasukkan nilai")