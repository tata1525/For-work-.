'''a=[5]
print(type(a))
print(a)

b={'История игрушек':1999}
print(type(b))
print(b)

#создание кортежа из одного элемента
c=(25,)
print(type(c))
print(c)

#Кортеж их разных типов
k=(50, 89.35, 'hello', None, True)
print(k[2])

#распаковка кортежа, переменных столько же, сколько элементов в кортеже
tu=(78, 'vibe', False, 98.9, 53)
a,b,c,d,e=(78, 'vibe', False, 98.9, 53)
print(a,b,c,d,e)

#сортировка кортежа
k3=('dont','kill','7897','apple')
print(tuple(sorted(k3)))


a=[]
for i in range(1,50):
    if i%3==0:
        a.append(i)
print(len(a))

#генератор списка
a=[i for i in range(1,50)]
print(a)

#генератор списка с условием
a=[i for i in range(1,50) if i%3==0]
print(a)


a=[]
for i in range(1,5):
    for j in range(1,5):
        a.append(i*j)           
print(a)

#генератор со вложенным циклом
a=[i*j for i in range(1,5) for j in range(1,5)]
print(a)

a=17
b=23
if a>b:
    print(a)
else:
    print(b)

#тернарный if: значение1 if условие else значение2
a=17
b=23
d=a if a>b else b
print(d)'''


k=[i for i in range(0,251) if i%15==0 or i%40==0]
print(k)


























