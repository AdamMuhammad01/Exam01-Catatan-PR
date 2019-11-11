
# def hello():
#     print('adam');
# hello();hello()



# def kuadrat(x):
#     print(x**2)
# kuadrat(2)
# kuadrat(5)

# def pangkat(x1, x2):
#     print(x1**x2)
# pangkat(2, 3)
# pangkat(5, 7)

# pangkat(
#      float(input('ketik angka 1: ')),
#      float(input('ketik angka 2: '))
#      )


#menentukan ganjil genap

# def a(x):
#     if x % 2 == 0:
#         print(x, 'termasuk GENAP');
#     else:
#         print(x, 'termasuk GANJIL')

# a(10)


def calc():
    x = float(input('masukkan angka 1 : '))
    y = input('masukkan operator aritmetika: ')
    z = float(input('masukkan angka 2: '))
    if y =='+':
         print(x+z)
    elif y =='-':
         print(x-z)
    elif y =='*':
         print(x*z)
    elif y =='/':
         print(x/z)
    else:
         print('operator tidak dikenali')
calc() 




# def vocal (kalimat):
#     kalimat = kalimat.replace('a','o')
#     kalimat = kalimat.replace('i','o')
#     kalimat = kalimat.replace('u','o')
#     print(kalimat)
# vocal('aiu')

# def salam():
#      print('selamat pagi')

# salam()


# def L_segitiga(alas, tinggi):            # %s >>> teks
#     Luas=(alas * tinggi)/2               # %d >>> desimal
#     print('luas segitiga: %d' %Luas)      #%f >>> pecahan

# L_segitiga(4,5)
