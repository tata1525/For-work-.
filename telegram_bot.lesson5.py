import telebot
import requests
import random
from bs4 import BeautifulSoup 

token='6218528481:AAGFNz-KuXfyytmmkIuq9MSRtsMzNKyXGiU'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text='Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!'
    bot.send_message(message.chat.id, welcome_text)

    
@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text='Нет, напрасно мы решили прокатить кота в машине: кот кататься не привык- опрокинул грузовик.'
    bot.send_message(message.chat.id, poem_text)

    
@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/').content
    html = BeautifulSoup(response, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link)
    
bot.polling()
