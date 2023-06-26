import random
'''class Human:
    name='Ivan'
    color_of_hair='red'
    height=190
    weight=90
    
human_obj=Human()
print(human_obj.name)
print(dir(Human))'''



'''class Human:

    def __init__(self, name, color_of_hair, height, weight):
        self.name=name
        self.color_of_hair=color_of_hair
        self.height=height
        self.weight=weight

        
human1=Human(name='Ivan', color_of_hair='red', height=190, weight=90)
human1.name='Александр'
human1.height=193
print(human1.name)


human2=Human(name='Alena', color_of_hair='green', height=156, weight=52)
print(human2.color_of_hair)'''




'''
class A:
    def one(self):
        print(1)
        
    def two(self):
        print(2)
        
class B(A):

    def two(self):
        print('two')

    def three(self):
        print(3)
        
print('B')        
b=B()
b.one()
b.two()
b.three()

print('A')               
a=A()
a.one()
a.two()
#будет ошибка
a.three()'''





class Tank:

    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model=model
        self.armor=armor
        self.damage=random.randint(min_damage, max_damage)
        self.health=health
        
    def print_info(self):
        print(f'{self.model} имеет броню {self.armor}мм при {self.health}ед. здоровья и урон в {self.damage} едениц')

    def health_down(self, enemy_damage):
        self.health-=enemy_damage
        print(f'\n{self.model}:')
        print(f'командир,по экипажу {self.model} попали, у нас {self.health} единиц здоровья')

        
    def shot(self, enemy):
         if self.health<=0 or self.damage>=self.health:
             self.health=0
             print(f'Экипаж танка {self.model} уничтожен')
         else:
              enemy.health_down(self.damage)
              print(f'\n{self.model}:')
              print(f'Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья')

class SuperTank(Tank):
    """Template of superTanks"""
    def __init__(self, model, armor,min_damage, max_damage, health):
        super().__init__(model, armor,min_damage, max_damage, health)
        self.forceArmor= True


    def health_down(self, enemy_damage):
         super().health_down(enemy_damage/2)

tank1=Tank('T-34', 90, 20, 30, 100)
tank2=Tank('Tiger', 120, 10, 50, 120)
tank1.print_info()
tank2.print_info()


tank1.shot(tank2)
tank1.shot(tank2)
tank1.shot(tank2)
tank1.shot(tank2)
tank1.shot(tank2)
tank1.shot(tank2)
tank1.shot(tank2)






































 




















