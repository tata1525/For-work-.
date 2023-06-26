import random
mon=['орёл','решка']
ans=input('Орёл или решка,что Вы выберите?')
ans_1=random.choice(mon)
if ans==ans_1:
    print('Вы победили!')
else:
    print('Вы проиграли')
