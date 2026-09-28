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