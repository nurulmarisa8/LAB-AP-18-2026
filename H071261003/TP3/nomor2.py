#DENAH KURSI BIOSKOP

while True:
    try:
        N = int(input("Masukkan jumlah baris:"))
        if N <= 0:
              print("Tidak boleh negatif")
              continue
        break
    except: 
         print("Input harus berupa angka")

while True:
    try :
        M = int(input("Masukkan jumlah kursi perbaris: "))
        if M <= 0:
            print("Tidak boleh negatif")
            continue
        break
    except:
         print("Input harus berupa angka")

for baris in range(1, N + 1):
    for kursi in range(1, M  + 1):

        if kursi == 13:
            continue

        if baris == 1:
            
            if kursi % 2 == 0:
        
                continue
        print(f"Baris {baris}, Kursi {kursi}")

        