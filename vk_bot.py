import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from course import get_course
from wiki import get_wiki_article

#авторизация токена
token='vk1.a.PnB250M0fBj1FIQ5o9o-l-Clz-Tu3lG4dgUoTHSvOMy-cXPhaPdgtcniOir9-D3ADGglDvBKSP1UHuW_tHCjXLKD9sx--k8Bg2SH6g3BKYQ9xyYxqLsd5yTNCziKnmoRfO7j3Shlj6j0Ra_xubZPJcXT3E_AsEC7mWQCBPYVxF9fss250bGZrn1rmFjUE7Jutgfp8sIEg63_eI-MaIpNJA'

vk_session=vk_api.VkApi(token=token)
vk=vk_session.get_api()

longpo11=VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type==VkEventType.MESSAGE_NEW and event.to_me:
        msg=event.text.lower()
        user_id=event.user_id

        random_id=random.randint(1,10**10)
        if msg=='-k':
            response='{0} рублей за 1 доллар\n{1} рублей за 1 евро\n '\
                      '{2} рублей за 10 юаней\n{3} рублей за 1 фунт\n'.format(
                          get_course('R01235'),
                          get_course('R01239'),
                          get_course('R01375'),
                          get_course('R01035')
                          )
            vk.messages.send(user_id=user_id, random_id=random_id, message=response)
        elif msg.starstwith('-в'):
            article=msg[2:]
            response=get_wiki_article(article)
        else:
            response='неизвестная команда'
        vk.messages.send(user_id=user_id, random_id=random_id, message=response)
    





















'''
#обработка сообщений
message=vk.method('messages.getConversations', {'count':20, 'filter':'unanswered'})'''

'''print(message['items'][0]['last_message'])
#id пользователя
id_1=message['items'][0]['from_id']
#id сообщения
id_m=message['items'][0]['last_message']['id']'''

'''while True:
    messages=vk.method('messages.getConversations', {'count':20, 'filter':'unanswered'})
    if messages['count']>=1:
        print(messages)'''

    
