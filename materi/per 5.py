
# andi= {'nama':'Andi','age':22,'is_married': False,
#        'job':'PNS','cars':['alpard', 'xenia', 'avenya'], 
#        'address':
#        {'street':'mawar ungu', 
#        'RT':5,
#        'Rw':12,
#        'kecamatan':'x',
#        'zipcode': 21345,
#        'geo':{'lat':134.1324,
#        'lng':47.89321}
       
#       }   
#         }
# print(andi['address']['kecamatan'])
# print(andi['nama'])
# print(andi['age'])
# print(andi['is_married'])
# print(andi.get('name'))
# print(andi.get('age'))
# print(andi.get('is_married'))

# print(andi.get('job', 'Maaf belum ada'))
# # print(andi['job'])
# print(type(andi))
# print(andi['cars'][2])
# print(andi['address']['geo']['lat'])

# andi['salary']=250000
# print(list(andi))
# print(andi['salary'])
# print(list(andi.keys()))
# print(list(andi.values()))



#senin = key; monday= values
# days={'senin':'monday','selasa':'tuesday','rabu':'wednesday','kamis':'thursday','jum\'at':'friday','sabtu':'saturday'}
# hari=input('ketik nama hari:')
# print(f'input bahasa inggrisnya:{hari.upper()} = {days[hari.lower()].upper()}')
# print(f'{hari.upper()}={days.get(hari.lower(), "ga ada!")}')

# hari=list(days)
# print(hari)
# day =list(days.values())
# print(day)
# x=input('ketik nama hari')
# if x.lower() in hari:
#     enghari=day[hari.index(x.lower())]
#     print(f'bahasa {x.lower()} adalah{enghari}')
# else:
#     idDay = hari[day.index(x.lower())]
#     print(f'bhs indo{x.lower()} adalah{idDay}')


# x=6
# if x == 4:
#     print('ini 4')
# else:
#     print('ini bukan 4')
    
    

# x=60
# if x < 10 :
#     print('x kurang dr 10')
# else:
#     print('x > dr 10')


# nilai=40
# if nilai >80:
#    print('anda lulus')
# elif nilai < 40:
#  print('anda blum lulus');
# else:
#     print('anda remedial')


# nilai=40
# if nilai >80:
#    print(f'nilai anda {nilai}, anda lulus')
# elif nilai < 40:
#  print(f'nilai anda {nilai},anda blum lulus');
# else:
#     print(f'nilai anda {nilai}, anda remedial')

# jomblo=False
# if jomblo:
#     print('anda single');
# else:
#     print('anda double')

# jomblo = True; jobless=True

# if jomblo == True and jobless == True:
#     print('anda kurang beruntung')
# elif jomblo == True and jobless == False:
#     print('selamat')
# elif jomblo == False and jobless ==True:
#     print('asda')
# else:
#     print('anda hebat')



# x=True;y=False

# x=2; y=5

# print(x<10 and y>10)


# nilai=98
# '''
# nilai >- 82 :A
# nilai 72-81 :B
# nilai 52-12 :C
# nilai <52   :E
# '''


# nilai=54
# if nilai >= 80:
#    print('A')
# elif nilai > 72 and nilai < 79:
#  print('B');
# elif nilai > 52 and nilai < 70:
#  print('C');
# else:
#     print('D')

# x={1:True, 2:False}
# print(list(x.items()))
