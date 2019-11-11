# python = lambda function
# x = lambda a:a
# def y (a, b, c):
#     return a+b+c
# print(x(2,3,4))
# print(y(2,3,4))


# def myFunction(x):
#     return lambda a:a**x

# pangkat2 = myFunction(2)
# pangkat3 = myFunction(3)
# pangkat4 = myFunction(4)


# print(pangkat2(3))


# x=[2,4,6,8,10]

# def pangkat2(a):
#     return a**2
# # y=map(pangkat2, x)   #cara 1
# # print(list(y))

# # z= map(lambda a:a**2, x)   #cara 2
# # print(list(z))


# b=[]
# for i in x:
#     b.append(i**2)         #cara 3    
# print(b)


# x = lambda a : True if a % 2 == 0 else False
# def y(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
# print(x(4))
# print(y(4))


# x= lambda a : print(a)
# print(x('hello'))

# def y(a):
#     return len(a)
# a = ['badu', 'rudi','joko']
# x = map(y, a)
# print(x)
# print(list(x))



# a =['nanas', 'madu', 'srikaya']
# b= ['sirsak', 'apel', 'delima']
# def combi(a,b):
#     return a+' '+b
# x = map(combi,a ,b)
# print(x)
# print(list(x))



# x= range(11)

# def kuranglima(x):
#     if x < 5:
#         return False
#     else:
#         return True
# y = filter(kuranglima, x)
# print(list(y))

# z= filter(lambda a:True if a>=0 else False, x)
# print(list(z))



# x=[1,3,5,6,8,9,90]
# y=[1,2,3,4,6,7]
# z=list(filter(lambda a: a in x, y))
# print(z)

# x = [1,2,3,4]
# hasil = 1
# for i in angka:
#     hasil *= i
# print(hasil)


# from functools import reduce
# z = reduce(lambda x, y: x*y, angka)
# print(z)


# kata=['ini', 'ibu', 'budi']
# print(' '.join(kata))


# angka=[1,2,4,5]
# z= list(map(lambda x:x*2, filter(lambda x:x>3, angka)))
# print(z)

# z=list(filter(lambda x:x>3, map(lambda x:x*2, angka)))
# print(z)



# from functools import reduce

# x= range(1, 102)
# z=list(map(lambda num:num*2, filter(lambda num:num%2==0,x)))
# y=reduce(lambda num,num1: num+num1, map(lambda num:num*2, filter(lambda num:num%2==0,x)))
# print(z)
# print(y)


# def prima(x):
#     a=false
#     if x>1:
#         if x==2
#         for i in range(2,x):
#             if x%i==0:
#                 return False
#                 break
#             else:
#                 return True
#     else:
#         return False
# print(prima(81))

