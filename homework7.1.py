from gtts import gTTS
from pygame import mixer
import pyaudio
import speech_recognition as sr
import random
import os


greetings=['Привет!','Hello!', 'Здравствуйте!', 'Hi', 'Доброго времени суток']

r=sr.Recognizer()
while True:
    with sr.Microphone(device_index=1) as sourse:
        print('Скажи что-нибудь')
        audio=r.listen(sourse)
    speech=r.recognize_google(audio, language='ru_RU', show_all=True)
    a=speech['alternative']
    a=a[0]
    a=a['transcript']
    if a=='Привет':
        my_file=open('homework7.txt', 'w')
        my_file.write(random.choice(greetings))
        my_string=my_file.read()
        my_file.close()

        mixer.init()
        tts=gTTS(text=my_string, lang='ru')
        tts.save('mp3_lesson11.mp3')
        mixer.music.load('mp3_hm7.mp3')
        mixer.music.play()
        
        
        
        
            

