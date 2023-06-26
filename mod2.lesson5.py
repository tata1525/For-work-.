import time
import random

'''
class RunningCode:
    def __init__(self):
        self.start=None

#вход в контекстный менеджер
    def __enter__(self):
        self.start=time.time()
        return self
    
#выход из контекстного менеджера, вычисление времени работы 
    def __exit__(self, exc_type, exc_val, exc_tb):
        t=time.time()-self.start
        print(f'Время работы программы: {t} сек.')

        if exc_type is TypeError:
            return True



with RunningCode() as t1:
    my_list=[i for i in range(1, 1000000)]
    my_list-='s' #ошибка  

my_list=[1,2,3,4,5]
list_iterator=iter(my_list)
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
'''

class RandomIter:
    def __init__(self, limit):
        self.limit=limit
        self.__reload=limit
    

    def __iter__(self):
        self.limit=self.__reload
        return self


    def __next__(self):
        if self.limit==0:
            raise StopIteration

        self.limit-=1
        return random.randint(0,99)
    
rand_iter=RandomIter(10)
print(iter(rand_iter))

for i in rand_iter:
    print(i)



























        
