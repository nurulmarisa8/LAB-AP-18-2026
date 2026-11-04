# class karyawan :
#     def __init__ (self, nama, gaji):
#         self.nama = nama
#         self.gaji = gaji

#     def info (self):
#         return f"nama : {self.nama} - Rp. {self.gaji}"

# class Manager (Karyawan) :
#     def __init__ (self, nama, gaji, tim):
#         super().__init__(nama, gaji)
#         self.tim = tim

#     def info (self):
#         return f"{super().info()} - Tim: {self.tim}"

# m = Manager ("Sari", 15000000, "IT")
# print (m.info())        

# class Rekening:
#     def __init__(self, pemilik, saldo=0):
#         self.pemilik = pemilik
#         self.saldo = saldo

#     def tarik(self, jumlah):
#         if jumlah > self.saldo:
#             return "Saldo tidak cukup"
#         self.saldo

