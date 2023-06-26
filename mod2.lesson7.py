from tkinter import*
import random

'''class Item:
    def __init__(self,name, price, weight):
        self.name=name
        self.price=price
        self.weight=weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price+other.price
        elif isinstance(other, int):
            return self.price+other
            
        

        
item_1=Item('Видеокарта', 60000, 0.8)
item_2=Item('Процессор', 90000, 0.3)


total_price=item_1+item_2
print(total_price)

new_price=item_1+1000
print(new_price)
'''


window=Tk()
window.geometry('600x600')
window.title('Алхимия')



    
class Energy:
    image=PhotoImage(file='energy.png').subsample(4,4)

    
class Swamp:
    image=PhotoImage(file='swamp.png').subsample(4,4)


class Clay:
    image=PhotoImage(file='clay.png').subsample(4,4)


class Fire:
    image=PhotoImage(file='fire.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay
       
    def __add__(self, other):
        if isinstance(other, Wind):
            return Energy 


class Water :
    image=PhotoImage(file='water.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Swamp


class Earth :
    image=PhotoImage(file='earth.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

    def __add__(self, other):
        if isinstance(other, Water):
            return Swamp


class Wind :
    image=PhotoImage(file='wind.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Energy
        


 
canvas=Canvas(window, width=600, height=600)
canvas.pack()
 
elements=[Fire(), Earth(), Water(), Wind()]

for elem in elements:
    img=canvas.create_image(random.randint(50,550), random.randint(50,550), image=elem.image)



def move(event):
    images_id=canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)

    if len(images_id)==2:
        elem_id_1, elem_id_2=images_id[0], images_id[1]
        element_1=elements[elem_id_1 - 1]
        element_2=elements[elem_id_2 - 1]
        
        new_element=element_1 + element_2

        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)                    


    canvas.coords(images_id, event.x, event.y)

window.bind('<B1-Motion>', move)

window.mainloop()













