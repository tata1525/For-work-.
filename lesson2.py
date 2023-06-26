import random
a=['булочка с корицей', 'котлетка', 'суши',' шаурма', 'бургер']
'''eat=random.choice(a)
print(eat)
print(random.randint(1,10))

for i in range(10):
    print('python')
print()  

n=4
k=0
while n>0:
    k+=1
    n-=1
print(k)'''

dohod=[]
print('Введите ваши доходы за последние шесть месяцев(через enter)')
for i in range(6):
    zp=int(input())
    dohod.append(zp*0.3)
print('Ваши наполения составят:',sum(dohod))
