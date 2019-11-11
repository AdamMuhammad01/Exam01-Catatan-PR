###########################  logical operator
# x = 5; y = '5'; z = 6

# print(x==int(y) and int(y)<z)
# print(x==int(y) or int(y)>z)
# print(not(x==int(y) or int(y)>z))

############################ if, elif, else

# nilai = 55
# if nilai > 80:
#  print("nilai A")
# elif nilai > 60 and nilai < 80:
#  print("nilai B")
# else :
#  print("anda tidak lulus")

################################

# nilai = 40
# if nilai > 80:
#     print(f'Nilai anda {nilai}, Selamat anda lulus!')
# elif nilai < 40:
#     print(f'Nilai anda {nilai}, tidak lulus')
# else:
#     print(f'Nilai anda {nilai}, mati aja')

###################################      contoh versi1
# jomblo = True; nganggur = True

# if jomblo == True and nganggur == True:
#     print('Anda jomblo pengangguran')
# elif jomblo == True and nganggur == False:
#     print('Anda kurang piknik')
# elif jomblo == False and nganggur == True:
#     print('Anda bucin laknat')
# else:
#     print('Anda cihuy bet')

###################################             contoh versi2
# jomblo = True; nganggur = True

# if jomblo and nganggur :
#     print('Anda jomblo pengangguran')
# elif jomblo and not nganggur:
#     print('Anda kurang piknik')
# elif not jomblo and nganggur:
#     print('Anda bucin laknat')
# else:
#     print('Anda cihuy bet')

##################################

'''
nilai >= 82 : A
nilai 72-81 : B
nilai 62-71 : C
nilai 52-61 : D
nilai <52 : E
'''
# nilai = 98
# if nilai >= 82:
#     print("Nilai Anda A")
# elif nilai > 71 and nilai < 82:
#     print("Nilai Anda B")
# elif nilai > 61 and nilai < 72:
#     print("Nilai Anda C")
# elif nilai > 51 and nilai < 62:
#     print("Nilai Anda D")
# else:
#     print("Nilai Anda E")
