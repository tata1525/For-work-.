import random

random_number=[]
for i in range(30):
    number=random.randint(0,5)
    random_number.append(number)
print('Количество пятерок в списке:', random_number.count(5))    
