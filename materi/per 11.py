# #class = cetakan object
# class Mobil:
#     warna:'merah'
#     tahun:2010

# #create object mobil1
# mobil1 = Mobil()
# mobil2 = Mobil()
# print(type(Mobil))




# class MobilCustom():
#     def __init__(self, warna, tahun, jenis):
#         self.color = warna
#         self.year = tahun
#         self.jenis = jenis

# # syntatic sugar
# mobil1 = MobilCustom('pink', 2018, 'sedan')
# mobil2 = MobilCustom('blue', 2010, 'truk')

# print(mobil1.jenis)
# print(mobil2.year)


'''
class MobilCustom():
    def __init__(self, warna, tahun, jenis):
        self.color = warna
        self.year = tahun
        self.jenis = jenis

# method
    def jadul(self):
         if self.year < 2010:
            return True
         else: return False
    def tes(self):
        print(self.color, self.year, self.jenis, self.jadul())

mobil1A = MobilCustom('merah', 1998, 'X')
mobil1B = MobilCustom('merah', 2018, 'Z')

print(mobil1A.tes())
print(mobil1A.year)
print(mobil1B.jadul())
'''

'''
class Mobil:
    def __init__(self, warna, seat):
         self.warna = warna
         self.seat = seat

class Car(Mobil):
    pass

mobil1 = Mobil('pink', 4)
car1 = Car('black', 8)
print(mobil1.warna, mobil1.seat)
print(car1.warna, car1.seat)
'''



'''
class X:
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar

class Y(X):
    def __init__(self, nama, gelar, univ):
        super().__init__(nama,gelar)
        self.kampus = univ

objX = X('Andi', 'M.Sc')
objY = Y('Budi', 'Dr.', 'UAI')
print(objY.nama, objY.gelar,objY.kampus)

print(objY.kampus)


from pprint import pprint
pprint(vars(objY))
'''

'''
class student:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

data=[
    {'nama':'andi', 'usia':21},
    {'nama':'bambang', 'usia':24},
    {'nama':'adi', 'usia':29},
    {'nama':'rudi', 'usia':26}
]

# nama = 'qwerty'
# vars()[nama] = 12345

# print(qwerty)

# def createObj(x):
#     nama = x['nama']
#     vars()[nama] = student(x['nama'], x['usia'])
#     return vars()[nama]

dataNew = list(map(lambda x:student(x['nama'], x['usia']),data))

print(dataNew[0].nama)
print(dataNew[0].usia)