print('Setup Denah Bioskop NontonYuk')

# Input baris dengan validasi
while True:
  try:
    baris = int(input('Masukkan jumlah baris: '))
    if baris <= 0:
      print('Jumlah baris harus lebih dari 0!')
    else:
      break
  except ValueError:
    print('Input baris harus berupa angka!')

# Input kursi per baris dengan validasi
while True:
  try:
    kursi_per_baris = int(input('Masukkan jumlah kursi per baris: '))
    if kursi_per_baris <= 0:
      print('Jumlah kursi harus lebih dari 0!')
    else:
      break
  except ValueError:
    print('Input kursi harus berupa angka!')

print('\nDaftar Kursi Tersedia')

for b in range(1, baris + 1):
  for k in range(1, kursi_per_baris + 1):
    # Aturan Mitos: Kursi 13 dilewati
    if k == 13:
      continue

    # Aturan Baris VVIP (Baris 1): Hanya kursi ganjil
    if b == 2 and k % 2 == 0:
      continue

    print(f'Baris {b} - Kursi {k}')