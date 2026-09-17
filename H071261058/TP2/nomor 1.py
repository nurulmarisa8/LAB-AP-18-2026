level_pedas = int(input("masukkan presentase cabai :"))

if level_pedas < 0 :
    print("tidak valid")
elif level_pedas <=10 :
    print("level aman")
elif level_pedas <=40 :
    print("level sedang")
elif level_pedas <=70 :
    print("level pedas")
else :
    print("level ekstrem")