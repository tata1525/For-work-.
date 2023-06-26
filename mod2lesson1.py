'''salary=200000
name='Danil'

print(f'У {name} зарплата в месяц {salary}')

#Реализация в виде словаря

baza={
    'name':'Danil',
    'salary':200000,
    }

#реализация с помощью списка со словарями
baza=[
    {'name':'Danil',
    'salary':200000},
    
     {'name':'Beatricks',
    'salary':1000000},

     {'name':'Kate',
    'salary':150000}
    ]
#увольняем сотрудника
print(baza)
for i in baza:
    if i['name']=='Kate':
        baza.remove(i)
        break
    
#Нанимаем сотрудника
new_emp={'name':'Lia','salary':380000}
baza.append(new_emp)

#Кол-во сотрудников
print(len(baza))'''

#Вывод информации о сотрудниках
#реализация с помощью класса

class Employee:
    def __init__(self, name, salary,on_vacation, is_good_employee):
        self.name=name
        self.salary=salary
        self.on_vacation=on_vacation
        self.is_good_employee=is_good_employee

    def get_info(self):
        return f'У {self.name} зарплата в месяц {self.salary}. В отпуске? - {self.on_vacation}. {self.name} хороший работник? - {self.is_good_employee}'

inf_baza=[Employee('Danil', 200000, 'да', True), Employee('Irina',1000000,'нет', False), Employee('Kate',380000,'да', True), Employee('Kirill',90000,'да', True),
Employee('Polina',45000,'нет', True)]

for i in inf_baza:
    if  ==False :
        inf_baza.remove(i)
        break
    


for i in inf_baza:
    print(i.get_info())
    

















