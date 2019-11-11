nama = 'adam & smith'  #string
usia = 15      # integer
tinggi = 175.3 #float
jomblo = True   #boolean
print('halo, aku ' + nama)
print('umurku', usia)
print(type(jomblo))
print('dan, aku', jomblo, 'jomblo')
print("hari ini hari jum'at")
print('Saya %s usia %d' %(nama, usia)) # lebih simple
print('saya {} usia {}'.format(nama, usia))
print(nama.upper())
print(nama.upper().islower())
print(len(nama))
print(nama[3])
print(nama[2:len(nama)])
print(nama.index('a'))

print(len(nama.replace(' ', '')))


