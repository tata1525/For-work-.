class user:

    def __init__(self,  health,damage):
        self.health=health
        self.damage=damage



    def enemy_damage(self, enemy_damage1):
        self.health-=enemy_damage1
        print(f'В меня попали, осталось {self.health} здоровья')
        
    def attack(self, enemy):
        enemy.enemy_damage(self.damage)
        print(f'У противника осталось {enemy.health} здоровья')       
    
        
class Magician(user):
     def __init__(self, health, damage):
        super().__init__(health, damage)
        
        
          
class Warrior(user):
     def __init__(self, health, damage):
        super().__init__(health, damage)
        

        
class Archer(user):
     def __init__(self, health, damage):
        super().__init__(health, damage)
        


        
magician1=Magician(150, 40)
warrior1=Warrior(145, 35)
archer1=Archer(160, 20)


print('Mаг применяет заклинание против воина:')
magician1.attack(warrior1)
print('Воин в ответ стреляет в мага:')
warrior1.attack(magician1)
print('Лучник стреляет в воина:')
archer1.attack(warrior1)
print('Лучник стреляет в мага:')
archer1.attack(magician1)
print('Маг применяет заклинание против лучника: ')
magician1.attack(archer1)
print('Воин стреляет в лучника:')
warrior1.attack(archer1)








        
