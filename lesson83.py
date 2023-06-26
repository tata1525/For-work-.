from pprint import pprint
from typing import Iterator


list_1=[
    {'name':'Iphone 14' , 'brand':'Apple' ,'price':1200},
    {'name':'Samsung Galaxy A53' ,'brand':'Samsung' ,'price':500 },
    {'name':'REALME C25s' ,'brand':'REALME' ,'price':400}
]

'''def item_price(item):
    return item['price']


print(sorted(list_1, key=item_price))'''

#лучщий вариант
'''pprint(sorted(list_1, key=lambda item: item['price']))'''

'''
apple_list=list(filter(lambda item: item['brand']=='Apple', list_1))
#print(isinstance(apple_list, Iterator))              
print(apple_list)



numbers=['1','2','3','4','5']

numbers=list(map(int,numbers))
print=(numbers)
'''

name_list=['Данил', 'Никита', 'Настя', 'Катя']
surname_list=['Петров', 'Иванов', 'Достоевская', 'Есенина']

'''full_name=list(map(lambda name, surname: f'{name} {surname}', name_list, surname_list))
print(full_name)


for name, surname in zip(name_list, surname_list):
    print(name, surname)
'''

index=[]

for i, item in enumerate(list_1):
    index.append({i:item})

pprint(index)



























