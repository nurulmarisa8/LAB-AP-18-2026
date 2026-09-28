# total hari dan barang yang terjual
total = 0

for hari in range(1,8):
    jumlah = int(input(f"Hari ke {hari}"))
    total += jumlah

print(total)
