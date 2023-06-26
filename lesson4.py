'''english_dict={'яблоко':'apple','молоко':'milk','кот':'cat'}

word=input('Введите слово на русском языке')
if word in english_dict:
    print(word,'на английском будет', english_dict[word])
else:
    print('Такого слова в словаре нет')

#films[film_1] равносильно films_get(film_1)
films={'Титаник':'Леонардо Ди Каприо', 'Гарри Поттер':'Том фелтон', ' Человек-паук':'Том Холланд'}
fav_actor='Леонардо Ди Каприо'
film_1=input('Введите название фильма')
if film_1 in films:
    actor=films.get(film_1)
    if actor==fav_actor:
        print('Этот фильм стоит посмотреть')
    else:
        print('Этот фильм смотреть не стоит')
else:
    print('Такого фильма в нашей базе нет')'''
        
#w=запись. r=чтение.r+= чтение и запись
#open- создали и открыли файл, второе- режим работы с файлом 
file=open('testfile103.txt', 'r')
#записали в файл фразу
file.write('hjdfjsdfjb')
#закрыли файл
for line in file.readlines():

#если уже есть название такого файла то он просто откроется 
#information=file.read

#print(information)
