import sys
import tkinter

WIDTH = 1000
HIGH = 800
p=tkinter.Tk()
d = tkinter.Canvas(bg="blue", width=WIDTH, height=HIGH)
d.pack()



def start(zveri):
    pass



def tick(zveri, pole):
    print('*')
    for i in range(0, WIDTH, 3):
        for o in range(0, HIGH, 3):
            eda = pole[o][i]['eda']
            d.create_rectangle(i,o,i+3,o+3,fill=f"#{hex(255-eda*2)[2:]*3}",outline=f"#{hex(255-eda)[2:]*3}")
    for i in zveri:
        d.create_rectangle(i.x, i.y, i.x+3, i.y+3,fill="red")
    d.pack()
    p.update()


