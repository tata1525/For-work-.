'''class Year:
    
    def __init__(self, days, season):
        self.__days=days
        self.__season=season

 
    def get_days(self):
        return self.__days


    def get_season(self):
        return self.__season
    

    def set_days(self, days):
        if days==365 or days==366:
            self.__days=days
        else:
            raise Exception('Некорректное значение')

    def set_season(self, season):
        if season=='зима' or season=='весна' or season=='осень' or season=='лето' :
            self.__season=season
        else:
            raise Exception('Некорректное значение')    
        


year=Year(365, 'зима')
print(year.get_days())
print(year.get_season())
year.set_days(366)
year.set_season('весна')
print(year.get_days())
print(year.get_season())
'''



class Person:
    def __init__(self, name, age):
        self.__name=name
        self.__age=age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name


    @name.deleter
    def name(self):
        del self.__name
        

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        if age>0:
            self.__age=age
            
        else:
            raise ValueError('Такого не может быть. Вы ещё не родились')


        
#или можно так записать
#if age<=0:
#        raise  ValueError('Такого не может быть. Вы ещё не родились')

        

    @age.deleter
    def age(self):
        del self.__age 
        

person=Person('Ivan',1)
print(person.name)
person.name='Danil'
print(person.name)
print(person.age)
del person.age
print(person.__dict__)







'''


class Year:
    
    def __init__(self, days, season):
        self.__days=days
        self.__season=season

    @property
    def days(self):
        return self.__days
    
    @days.setter
    def days(self, days):
        if days==365 or days==366:
            self.__days=days
        else:
            raise Exception('Некорректное значение')

    @property
    def season(self):
        return self.__season
    
    @season.setter
    def season(self, season):
        if season=='зима' or season=='весна' or season=='осень' or season=='лето' :
            self.__season=season
        else:
            raise Exception('Некорректное значение')


year=Year(365, 'зима')
print(year.days)
print(year.season)
year.days=366
year.season='весна'
print(year.days)
print(year.season)


'''



























    
 
