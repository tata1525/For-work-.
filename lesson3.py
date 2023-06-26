import random

actor=input('Кто играет главную роль в фильме?')
rating=int(input('Какой рейтинг у этого фильма?'))
#задаем переменной значение строки
actor_1='Леонардо ди Каприо'

if actor==actor_1 and rating>7:
    print('Этот фильм точно надо смотреть.')
#если нужно прописать еще какое-то условие ( вместо else: if  употребляют elif)    
elif actor==actor_1 or rating>7:
        print('Должен быть неплохой фильм.')
else:
    print('Это не стоит смотреть.')


number_1=random.randint(1,10)
number=int(input('Попробуйте угдать число, загаданное компьютером от 1 до 10. Введите число:'))
if number==number_1:
    print('Поздравляем! Вы угадали.')
elif number-number==1 or number-number_1==-1:
    print('Вы почти угадали!')
else:
    print('Сoчувствуем. Вы не угадали.')
    
