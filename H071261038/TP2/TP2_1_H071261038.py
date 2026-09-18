# Soal 1
persentase = int(input("Masukkan persentase cabai: "))

if persentase < 0:
    print("input tidak valid")
elif persentase <= 10:
    print("level aman")
elif persentase <= 40:
    print("level sedang")
elif persentase <= 70:
    print("level pedas")
else:
    print("level ekstrim")








