def strcounter(s):
    for sym in set(s):  #представили строку как множество - содержит  уникальные элементы и позволяет получить уникальные элементы,  убрали повторения
        counter=0
        for sub_sym  in s:
            if sym==sub_sym:
                counter+=1

        print(sym, counter)
        
strcounter('aaaaaaaaaaaaaaaaaaaaaabcd')

'''
b='nnnnnnnnry'
print(set(b))
'''

