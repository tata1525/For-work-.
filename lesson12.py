from datetime import datetime
'''a =1

print(id(a), type(a))
print(id(id), type(id))
print(id(type), type(type))


class A:
    def public(self):
        return 42
    def _private(self):
        return 'test'
    def __protect(self):
        return True
    def wrapper_protect(self):
        return self.__protect()
        



a=A()
print(a.public())
print(a._private())
print(a._A__protect())
print(a.wrapper_protect())'''






def timeit(func):
    def wrapper(val):
        start=datetime.now()
        res=func(val)
        end=datetime.now()
        print(f'time{end-start}')
        return res

    return wrapper





@timeit
def get_list_1(val):
    return [i for i in range (val) if i%2==0]


@timeit
def get_list_2(val):
    new_list=[]
    for i in range (val):
        if i%2==0:
            new_list.append(i)        
    return new_list

val=100000

a=get_list_1(val)
b=get_list_2(val) 
print(a)
print(b)

























