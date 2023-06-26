from gtts import gTTS
from pygame import mixer
import pyaudio
import speech_recognition as sr
import random
import os


films=['Тайна Коко','Душа','фильмы о Гарри Поттере','Титаник','Один дома','Аватар']

r=sr.Recognizer()
def hint():
    while True:
        with sr.Microphone(device_index=1) as sourse:
            print('Привет! Скажи,чем я могу помочь?')
            audio=r.listen(sourse)
        speech=r.recognize_google(audio, language='ru_RU', show_all=True)
        a=speech['alternative']
        a=a[0]
        a=a['transcript']
        if a=='Выбери фильм':
            mixer.init()
            tts=gTTS(text='Советую посмотреть'+random.choice(films), lang='ru')
            tts.save('mp3_homework71.mp3')
            mixer.music.load('mp3_homework71.mp3')
            mixer.music.play()
            
hint()
