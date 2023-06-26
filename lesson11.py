import os
from pygame import mixer
from gtts import gTTS


my_file=open('lesson11.txt', 'r')
my_string=my_file.read()
my_file.close()

mixer.init()

tts=gTTS(text=my_string, lang='ru')
tts.save('mp3_lesson11.mp3')
mixer.music.load('mp3_lesson11.mp3')
mixer.music.play()
#os.remove('mp3_lesson11.mp3') удаление файла

