print("--- Setup Denah Bioskop Nonton Yuk ---")
while True:
    try: 
        baris = int(input("masukkan jumlah baris: "))
    except:
        print("input baris harus berupa angka!")
        continue
    if baris <= 0 :
        print("jumlah baris harus lebih dari 0!")
        continue
    break

while True:
    try: 
        kursi = int(input("masukkan jumlah kursi per baris: "))
    except:
        print("input kursi harus berupa angka!")
        continue
    if kursi <= 0 :
        print("jumlah kursi harus lebih dari 0!")
        continue
    break

print("--- daftar kursi tersedia ---")

for baris in range (1, baris+1 ):
    for kursi in range (1, kursi+1) :
        if kursi == 13 :
            continue
        if baris == 1 and kursi %2 == 0 :
            continue
        print(f"baris {baris} - kursi {kursi}")