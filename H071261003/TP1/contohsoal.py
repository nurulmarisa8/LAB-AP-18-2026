menu = ["Pulpen", "Buku", "Pensil"]
harga = [5000, 10000, 3000]
jumlah = [2, 3, 4]

sub_pulpen = harga[0] * jumlah[0]
sub_buku = harga[1] * jumlah[1]
sub_pensil = harga[2] * jumlah[2]

sub_total = [sub_pulpen, sub_buku, sub_pensil]
total_pendapatan = sum(sub_total)

print ("Subtotal Puplen:", sub_pulpen)
print ("Subtotal Buku", sub_buku)
print ("subtotal Pensil", sub_pensil)
print ("Subtotal:", sub_total)
print ("Subtotal Pendapatan:", total_pendapatan)
       
