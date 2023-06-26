import random

animals=['кот', 'олень', 'попугай']
des=['пушистый', 'большой', 'голубой']
for i in range(3):
    print(random. choice (des)+' ', random. choice (animals))
       
#другой вариант программы


animals=[]
des=[]
print('Введите названия трех животных(через enter)')    
for i in range(3):
    an=input()
    animals.append(an)
print('Введите прилагательные,описывающие этих животных(через enter)')
for i in range(3):
    de=input()
    des.append(de)
for i in range(3):
    print(random.choice(des)+' ',random.choice(animals))   
