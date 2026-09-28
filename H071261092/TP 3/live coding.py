print("total barang terjual selama 7 hari")
total_barang = 0
hari = 1
while hari <= 7:
    try:
        jumlah = int(input(f"Hari ke-{hari}: "))
        
        
        if jumlah < 0:
            print("Jumlah barang tidak boleh negatif!")
            continue
            
        total_barang += jumlah
        hari += 1  
        
    except:
        print("Input tidak valid! Masukkan angka bulat.")

print(f"Total barang terjual = {total_barang}")