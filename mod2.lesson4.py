import time
import contextlib


'''my_iter=[time.sleep(x) for x  in range(1,3)] #Строгое вычиcление
print(my_iter)

my_iter2=(time.sleep(x) for x  in range(1,3)) #Ленивое вычиcление
print(my_iter2)

#Ленивые вычисления в виде функции

def my_lazy(items):
    for item in items:
        yield item
        
#альтернативная запись первой функции(схлопнуть 2 последние строки)
def my_lazy(items):
    yield from items
    


for item in my_lazy([1,2,3,4,5]):
    print(item)

 
    

items=['Яблоко','Банан','Апельсин']

for i in my_lazy(items):
    print(i)'''







'''my_file= open('test105.txt', 'w')

my_file.write('Writing some info...')

my_file.close()'''


with open('test105.txt', 'w') as my_f:
    my_f.write('Writing some info...')
    print(my_f.closed) #False

print(my_f.closed) #True
    


#Контекстный менеджер по развороту строки

@contextlib.contextmanager
def str_revers(my_str):
    print('входим в контекстный менеджер:')
    yield my_str[::-1]
    print('выходим из контекстного менеджера')
    
    
with str_revers('Hello, world!') as str2:
    print(f'Выполняется код: {str2}')





@contextlib.contextmanager
def exc_handler(exc):
    try:
        yield True
    except exc:
        ('Произошло исключение')

with exc_handler(IndexError):
    my_l=[1,2]
    print(my_l[3])
    
























































 















    
