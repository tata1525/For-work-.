class Human:

    def __init__(self, name, color_e, color_h, age, height):
        self.name = name
        self.color_e = color_e
        self.color_h = color_h
        self.age = age
        self.height = height

    def getInfo(self):
        return f'мужчина {self.name}  цвет глаз {self.color_e} цвет волоc {self.color_h} возраста {self.age} роста {self.height}'
        

human1 = Human('Ivan', 'blue', 'blond', 22, 196)

print(human1.getInfo())
