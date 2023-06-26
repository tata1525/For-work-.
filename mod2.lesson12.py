import os

current_path=os.path.abspath(__file__) #__file__ указывает на текущий файд ; в переменной current.. cодержится абсолютныйпуть до текущего файла

parent_path=os.path.join(current_path, '..', '..')

print(current_path)
print(parent_path)



#рекурсия- вызов функции внутри самой себя
'''
def recurs(count):
    print(count)
    if count==5:
        return
    recurs(count+1)
    print(count)
'''

def get_all_files(path):
    for i_name in os.listdir(path):
        new_path=os.path.join(path, i_name)
        if os.path.isdir(new_path):
            print('python', i_name)
            get_all_files(new_path)
        else:
            print('-', i_name)

get_all_files(parent_path)
