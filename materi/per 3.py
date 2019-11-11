'''
# ayam = 13-kambing => B
# 2* (13-kambing)+4*kambing = 32
# kakiA * (jmlTot - JmlK) + kakiK* jmlK = jmlKaki
# -(kA*jK)+(kK*jK)=jKaki-(kA*jT)
# jk*(kK-kA)=jKaki-(kA*jT)
# jK=(jKaki-(kA*jT))/(kK-kA)
# jK=(32-(2*13))/(4-2)
# Dari Pers A => kambing = 13 - ayam
# 2*ayam+4*(13-ayam) =32
# (kA*jA)+(kK*jT-(kK*jA) = jKaki

# jA=(jKaki-(kA*jT))/(kK-kA)
# jA=(jKaki-(kA*jT))/(kA-kA)


jmlH = 13; jmlKaki = 32; kakiA = 2; kakiK = 4;
A=(jmlKaki-(kakiK*jmlH))/(kakiA-kakiK)
K=(jmlKaki-(kakiA*jmlH))/(kakiK-kakiA)
print(f'jumlah ayam={A}')
print(f'jumlah kambing={K}')
'''


# x=12
# x=16
# x+=423 # x=x+2
# x-=435 # x=x-2
# x *= 23
# x-=54
# print(x)


# memanggil 
# x='qrwdhygwhgiuhgiuwrghiwrgiuh'
# print(x[::3])
# print(x[2:9:3])
# print(x.count('g'))


# kalimat='HhHhHhHHHhHhHhHhHhHhHhH'
# cari='h'
# print(cari.lower()in kalimat.lower())
# print(kalimat.lower().count(cari.lower))






#list


# x=['rudi', 'gandi', 'lusi']
# print(x[0])
# print(type(x[0]))
# print(type(x))
# print(x[len(x)-2])




# hari=[ 'mon', 'tue', 'thur', 'fri']
# print(hari[2])



hari=[ 'sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat']
now='wed'; brpHari=-100
iNow=hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari=hari[(iNow+sisaHari)%7]
print(hariYgDicari)
hari[6]='libur'
print(hari)
hari.append('seninsenin')
print(hari)
hari.insert(8, 'seninisenin')

# hari.remove('seninsenin')
# print(hari)
# hari.remove('seninisenin')
# print(hari)
# hari.pop(2)
# print(hari)
# hari.sort() #mengurutkan konten
# print(hari)
# hari.reverse() #index terbalik
# print(hari)


# x=1242346
# print(type(str(x)))


# x=[1, 231, 4, 24, 52, 58]
# y=x[::2]
# print(x+y)

# z=[[1, 2,5],[6, 7,8 ],[4, 5, 7]]
# print(z[0][2])