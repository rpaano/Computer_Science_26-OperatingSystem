from time import sleep
import tkinter as tk
from random import randint
from _thread import start_new_thread

in_women = 0
in_men = 0  

x_men = 515
y_men = 135

x_women = 515
y_women = 185

root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=300)
canvas.pack()

canvas.create_text(400,90,fill="darkblue",font="Times 15 italic bold",text="MEN'S LINE")
canvas.create_text(400,230,fill="darkblue",font="Times 15 italic bold",text="WOMEN'S LINE")
canvas.create_text(815,100,fill="darkblue",font="Times 10 italic bold",text="TOILET")
canvas.create_text(915,100,fill="darkblue",font="Times 10 italic bold",text="EXIT")
canvas.create_text(400,50,fill="darkblue",font="Times 10 italic bold",text="PRESS ENTER TO START")

def men(x_men):
    #global x_men
    global y_men
    canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='red',outline="blue",width=3)
    x_men += 100

def main(event):
    global x_men
    count = 0
    while count < 1:
        start_new_thread(men,(515,))


#5
root.bind('<Return>',main)     
root.mainloop()


