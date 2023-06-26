from bs4 import BeautifulSoup
import requests
from datetime import datetime
from tkinter import*


window=Tk()
window.geometry('400x350+300+300')
window.title('Курс валют')
window.resizable(width=False, height=False)
window['bg']='light blue'


url='http://www.cbr.ru/scripts/XML_daily.asp?'

today=datetime.today()
today=today.strftime('%d/%m/%Y')

payload={'date_req':today}

response=requests.get(url, params=payload)

xml=BeautifulSoup(response.content, 'html.parser')


def getCourse(id):
    return xml.find('valute', {'id':id}).value.text


img_logo=PhotoImage(file='logo.png')
logo=Label(window, image=img_logo, bg='lavender')
logo.place(x=0,y=0)


lab=Label(window, text='Курс валют\n Maximum-банк', fg='black',bg='lavender', font='Arial 22')
lab.place(x=150,y=25)


course_info=Label(window, text='Курс на: '+today.replace('/','.'),bg='lavender', font='Arial 18')
course_info.place(x=100,y=190)


usd_course=Label(window, text='$'+getCourse('R01235'),bg='lavender', font='Arial 18')
usd_course.place(x=150,y=220)


cny_course=Label(window, text='CNY: '+getCourse('R01375'),bg='lavender', font='Arial 18')
cny_course.place(x=130,y=250)


window.mainloop()
