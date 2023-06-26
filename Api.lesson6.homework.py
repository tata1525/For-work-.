import requests
from bs4 import BeautifulSoup
from datetime import datetime

url='http://www.cbr.ru/scripts/XML_daily.asp?'

today=datetime.today()
today=today.strftime('%d/%m/%Y')

payload={'date_req':today}
response=requests.get(url, params=payload)
xml=BeautifulSoup(response.content, 'html.parser')




valute_from='EUR'
valute_to='USD'
def getCourse(id):
    return xml.find('valute', {'id':id}).value.text

RUR_in_EUR=getCourse('R01239')
RUR_in_USD=getCourse('R01235')
print(RUR_in_EUR)
R_in_E=int(input('Перезапишите число сверху, окргулив до целого числа:'))
print(RUR_in_USD)
R_in_U=int(input('Перезапишите число сверху, округлив до целого числа:'))          

amount=int(input('Введите сумму денег,которую вы хотите конвертировать:'))
def course(valute_from, valute_to, amount):
    if valute_from=='RUR':
     return amount/R_in_U
    
    elif valute_from!='RUR':
        amount=amount*R_in_E
        return amount/R_in_U
        
print('Конвертированная сумма:',course(valute_from, valute_to, amount))            

    
    
