from tkinter import*
import random

#шаблон окна
window=Tk()

#задаем размеры окна. можно так - '600'x'600'
w=600
h=600
window.geometry(str(w)+'x'+str(h))

window.title('Game Knight&Dragons')


#холст для отрисовки игрового поля(крепим на него)
canvas=Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)


#фон для игры
bg_photo=PhotoImage(file='bg_2.png')

#Класс рыцарь
class Knight:
    def __init__(self):
        #координаты центра рыцаря
        self.x=70
        #//-деление нацело-только целое число будет браться
        self.y=h//2
        #скорость рыцаря ( в начале игры он стоит)
        self.v=0
        #изображение рыцаря
        self.photo=PhotoImage(file='knight.png')


     #движение вверх
    def up(self, event):
          self.v=-3
          
     #движение вниз     
    def down(self,event):
          self.v=3
              
     #остановка
    def stop(self, event):
         self.v=0

#Класс дракон
class  Dragon:
    def __init__(self):
        self.x=750
        self.y=random.randint(100,500)
        self.v=random.randint(1,3)
        self.photo=PhotoImage(file='dragon.png')

knight=Knight()

dragons=[]
for i in range(3):
    dragons.append(Dragon())

def game():
    canvas.delete('all')
    canvas.create_image(300,300, image=bg_photo)
    canvas.create_image(knight.x,knight.y,image=knight.photo)
    knight.y+=knight.v

    current_dragon=0
    dragon_to_kill=-1

    for dragon in dragons:
        dragon.x-=dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

        if ((dragon.x-knight.x)**2)+((dragon.y-knight.y)**2)<=(96)**2:
            dragon_to_kill=current_dragon

        current_dragon+=1

        if dragon.x<=0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text='You lose!', font='Verdana 42', fill='red')
            break

    if dragon_to_kill>=0:
            del dragons[dragon_to_kill]


    if len(dragons)==0:
        canvas.delete('all')
        canvas.create_text(w//2, h//2, text='You win!', font='Verdana 42', fill='red')
    else:
        window.after(5, game)
            
        
game()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)



#эта строка всегда последняя
window.mainloop()
