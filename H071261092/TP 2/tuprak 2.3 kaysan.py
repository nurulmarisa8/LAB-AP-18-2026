nilai_tes = int(input("masukkan nilai tes : "))
if nilai_tes >= 80:
    print("Anda lolos ke tahap wawancara")
else: 
    pengalaman = int(input("masukkan pengakaman kerja anda (tahun) : "))
    if nilai_tes >= 65 and pengalaman >= 2:
        print ("anda lolos bersyarat")
    else:
        print("anda tidak lolos")