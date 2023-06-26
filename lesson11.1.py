import pyaudio
import speech_recognition as sr

r=sr.Recognizer()
while True:
    with sr.Microphone(device_index=1) as sourse:
        print('Привет! Скажи что-нибудь...')
        audio=r.listen(sourse)
    speech=r.recognize_google(audio, language='ru_RU', show_all=True)
    a=speech['alternative']
    a=a[0]
    print(a['transcript'])
        
    
