# Denah Kursi Bioskop

print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        n_baris = int(input(" Masukkan jumlah baris: "))
        if n_baris <= 0:
            print ("Jumlah baris harus lebih dari 0!")
            continue
        break
    except:
        print("Input baris harus berupa angka!")

# Input jumlah kursi per baris
while True:
    try:
        n_kursi = int(input("Masukkan jumlah kursi perbaris: "))
        if n_kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except:
        print("Input kursi harus berupa angka!")
        continue
    
    print("--- Daftar Kursi Tersedia ---")

# Nested Loop 
for baris in range(1, n_baris + 1):
    for kursi in range(1, n_kursi + 1):
        # Atur Mitos: Kursi nomor 13 dilewati
        if kursi == 13:
                continue

        # Atur barisan VVIP (Baris 1): Hanya kursi ganjil
        if baris == 1 and kursi % 2 == 0:
            continue
        print(f"Baris {baris} - Kursi {kursi}")
