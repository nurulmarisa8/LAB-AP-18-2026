hari = 5
total_tabungan = 0
while hari >0 :
    jumlah_tabungan = int(input(f"Masukkan jumlah tabungan hari ke-{hari}: "))
    total_tabungan += jumlah_tabungan
    hari -= 1
print(f"Total tabungan = Rp{total_tabungan}")
if total_tabungan >= 100000 :
    print("target tabungan tercapai!")
else:
    print("target tabungan belum tercapai.")