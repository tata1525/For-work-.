deg=int(input('Сколько градусов сейчас на улице?'))
if deg<=-20:
    print('Очень холодно')
elif deg==-10:
    print('Холодно')
elif deg==0:
    print('Прохладно')
elif deg==5:
    print('Тепло')
elif deg==20:
    print('Жарко')
elif deg>=30:
    print('Очень жарко')
else:
    print('Ошибка. Извините,в нашей базе нет таких значений')

