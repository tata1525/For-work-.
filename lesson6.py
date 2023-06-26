import requests
from bs4 import BeautifulSoup
from datetime import datetime

url='http://www.cbr.ru/scripts/XML_daily.asp?'

today=datetime.today()
today=today.strftime('%d/%m/%Y')

payload={'date_req':today}
#подключаемся к сайту с xml документом
response=requests.get(url, params=payload)
#'xml'
xml=BeautifulSoup(response.content, 'html.parser')


def getCourse(id):
    return xml.find('valute', {'id':id}).value.text

print(getCourse('R01235'),'рублей за 1 доллар')
print(getCourse('R01150'),'рублей за 1 вьетнамский донг')
print(getCourse('R01035'),'рублей за 1 Фунт стерлингов Соединенного королевства')

