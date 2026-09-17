# nomor 2

jarak = int(input("Masukkan jarak pengirimanan (KM) :"))
express =(input("Layanan express (ya/tidak) :"))

if jarak <=0 :
    print("jarak tidak valid")
elif jarak <= 5 :
    jarak = 10000
elif jarak <= 20 :
    jarak = 20000
else :
    jarak = 35000

layanan = 15000 if express == ("ya") else 0 
tarif = jarak + layanan
print("total tarif pengiriman :  RP", tarif)