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

#9
def random_gen():
    return randint(1, 9)
#8
def waiting():
    num = random_gen()
    sleep(num)
    

def move(men):
    canvas.move(men,100,0)

#7.1.1
def men1_move_x():
    
    global in_men
    global in_women
    waiting()
    ctr = 0
    while True:
        if in_women == 0:
            break

    in_men += 1          
    while ctr < 30:
        sleep(0.05)
        canvas.move(men1,10,0)
        ctr += 1

    waiting()
    in_men -= 1
    move(men1)
    

#7.1.2
def men2_move_x():
    global in_men
    global in_women
    waiting()
    ctr = 0
    while True:
        if in_women == 0:
            break

    in_men += 1
    
    waiting()
    
    while ctr < 20:
        sleep(0.05)
        canvas.move(men2,10,0)
        ctr += 1

    waiting()
    in_men -= 1
    move(men2)

#7.1.3
def men3_move_x():
    global in_men
    global in_women
    waiting()
    ctr = 0
    while True:
        if in_women == 0:
            break

    in_men += 1  
    waiting()
    
    while ctr < 10:
        sleep(0.05)
        canvas.move(men3,10,0)
        ctr += 1

    waiting()
    in_men -= 1
    move(men3)

#7.2.1
def women1_move_x():
    
    global in_men
    global in_women
    waiting()
    ctr = 0
    while True:
        if in_men == 0:
            break

    in_women += 1
    waiting()
    
    while ctr < 30:
        sleep(0.05)
        canvas.move(women1,10,0)
        ctr += 1

    waiting()
    in_women -= 1
    move(women1)

#7.2.2
def women2_move_x():
    global in_men
    global in_women
    waiting()
    ctr = 0
    while True:
        if in_men == 0:
            break

    in_women += 1
    waiting()
    
    while ctr < 20:
        sleep(0.05)
        canvas.move(women2,10,0)
        ctr += 1

    waiting()
    in_women -= 1
    move(women2)

#7.2.3
def women3_move_x():
    global in_men
    global in_women
    waiting()
    ctr = 0
    while True:
        if in_men == 0:
            break

    in_women += 1
    waiting()
    
    while ctr < 10:
        sleep(0.05)
        canvas.move(women3,10,0)
        ctr += 1

    waiting()
    in_women -= 1
    move(women3)
    
def waiting1():
    sleep(randint(9, 20))

#7.1
def men():
    global in_women
    global in_men
    waiting()

    while True:
        if in_women == int(0):
            break
       
    start_new_thread(men1_move_x,())
    
    start_new_thread(men2_move_x,())
    
    start_new_thread(men3_move_x,())
    
    
#7.2
def women():
    global in_women
    global in_men
    
    waiting()
    
    
    while True:
        if in_men == int(0):
            break

    start_new_thread(women1_move_x,())
    
    start_new_thread(women2_move_x,())
    
    start_new_thread(women3_move_x,())

#6
def main(event):

    global in_men
    global in_women
    in_men = 0
    in_women = 0
    start_new_thread(men,())
    
    start_new_thread(women,())

#1
root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=300)
canvas.pack()

in_women = 0
in_men = 0

#2
cr_men = canvas.create_rectangle(800,200,830,120,outline="brown",width=3)

#3.1
men1 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='red',outline="blue",width=3)
x_men += 100

men2 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='blue',outline="blue",width=3)
x_men += 100

men3 = canvas.create_oval(x_men-10,y_men-10,x_men+10,y_men+10,fill='brown',outline="blue",width=3)
x_men += 100

#3.2
women1 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='green',outline="yellow",width=3)
x_women += 100

women2 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='yellow',outline="yellow",width=3)
x_women += 100

women3 = canvas.create_oval(x_women-10,y_women-10,x_women+10,y_women+10,fill='violet',outline="yellow",width=3)
x_women += 100

#4
canvas.create_text(400,90,fill="darkblue",font="Times 15 italic bold",text="MEN'S LINE")
canvas.create_text(400,230,fill="darkblue",font="Times 15 italic bold",text="WOMEN'S LINE")
canvas.create_text(815,100,fill="darkblue",font="Times 10 italic bold",text="TOILET")
canvas.create_text(915,100,fill="darkblue",font="Times 10 italic bold",text="EXIT")
canvas.create_text(400,50,fill="darkblue",font="Times 10 italic bold",text="PRESS ENTER TO START")

#5
root.bind('<Return>',main)     
root.mainloop()
