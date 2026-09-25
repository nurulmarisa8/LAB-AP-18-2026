total_barang = 0

for i in range (1, 8):
    terjual = int(input(f"hari ke-{i}: "))
    total_barang += terjual

print(f"total barang terjual = {total_barang}")