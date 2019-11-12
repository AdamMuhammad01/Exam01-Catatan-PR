                                                                                ###########soal no 1


'''
a = {2,4,6,8,10,12,14,16,18}
b = {1,3,5,7,9,11,13,15,17,19}
c= {-10,-9,-8, -7, -6,-5, -4, -3, -2, -1}
d = {2,3,5,7,11,13,17,19}
e = {4,6,8,9,10,12,14,16,18,20}


f=a.union(b)
g=d.union(e)

h = f.union(g.union(c))
print('no 1 a :', h)                                                  #soal 1.a

i = a.intersection(b)
j = d.intersection(e)
k = i.union(j)
print('no 1 b :',k)                                                   #soal 1.b

l = f.intersection(g)
print('no 1 c :',l)                                                   #soal 1.c

m = f-g
print('no 1 d:',m)                                                    #soal 1.d
n=f.union(c) 
o=a.intersection(e)
p=n-o
print('no 1 e:',o)                                                    #soal 1.e


'''




                                                                    ##################soal no.2

'''

segitigakata = 'PurwadhikaStartupandCodingSchool@BSD'
x = 0
mulai = 0
end = 0
done = False
while not done:
    mulai = end
    while segitigakata[mulai] == 'P':
        mulai  += 1
    end = mulai + x + 1
    if end > len(segitigakata):
        end = len(segitigakata)
        done = True
    print(segitigakata[mulai:end])
    x += 1


print('belum selesai')
'''





                                                                    #####################soal no.3
'''
import json

with open('ccNasabah.json', 'r')as x:
     out = json.load(x)


data = json.load(open('ccNasabah.json', 'r'))
data = json.load(open('ccNasabah.json', 'r'))

with open('ccNasabah.json', 'w') as y:
    json.dump(out, y)
    print(type(out))
    print(type(out[0]))


'''