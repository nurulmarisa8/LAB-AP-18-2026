print('Rekapitulasi Transaksi Dins Store')
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")

while True:
  try:
    item = int(input('Masukkan jumlah item: '))

    if item == 0:
      print('Toko ditutup. Sesi rekap selesai.')
      break
    elif item < 0:
      print('Jumlah tidak boleh negatif')
    elif item > 100:
      print('Maksimal 100 item per transaksi!')
    else:
      print(f'Transaksi {item} item berhasil!')

  except ValueError:
    print('Input harus berupa angka!')



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
    if b == 1 and k % 2 == 0:
      continue

    print(f'Baris {b} - Kursi {k}')

Input total kursi bus dengan validasi



while True:
  try:
    kuota = int(input('Masukkan maksimal kursi bus: '))
    if kuota <= 0:
      print('Jumlah kursi harus lebih dari 0!')
    else:
      break
  except ValueError:
    print('Input jumlah kursi harus berupa angka!')

print('\nSistem Reservasi PO BUS Dimulai')

total_pendapatan = 0

while kuota > 0:
  print(f'Sisa kursi: {kuota}')
  try:
    umur = int(input('Masukkan umur penumpang: '))

    if umur < 0:
      print('Umur tidak valid!')
      continue

    if 0 <= umur <= 5:
      harga = 0
      print('Kategori: Balita')
      print('Tiket Gratis (Rp 0)')
    elif 6 <= umur <= 12:
      harga = 50000
      print('Kategori: Anak | Harga: Rp 50.000')
    else:
      harga = 100000
      print('Kategori: Dewasa | Harga: Rp 100.000')

    total_pendapatan += harga
    kuota -= 1

  except ValueError:
    print('Input umur harus berupa angka!')

print('\nSemua Kursi Terisi')
print(f'Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}')